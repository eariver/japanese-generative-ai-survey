#!/usr/bin/env bash
set -u

raw_dir="$(dirname "$0")/raw"
target_file="$(dirname "$0")/capture-targets.tsv"

capture_one() {
  local task="$1"
  local url="$2"
  local source_class="$3"
  local filename="$4"
  local capture_time
  local status
  capture_time="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  status="$(curl -L --silent --show-error --max-time 20 -D "$raw_dir/$filename.headers" -o "$raw_dir/$filename" -w '%{http_code}\t%{content_type}\t%{size_download}' "$url" 2>"$raw_dir/$filename.curl-stderr" || true)"
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$task" "$capture_time" "$source_class" "$filename" "$url" "$status"
}

active=0
while IFS=$'\t' read -r task url source_class filename; do
  [ -n "$task" ] || continue
  if [ "$active" -ge 8 ]; then
    wait -n || true
    active=$((active - 1))
  fi
  capture_one "$task" "$url" "$source_class" "$filename" &
  active=$((active + 1))
done < "$target_file"
wait
