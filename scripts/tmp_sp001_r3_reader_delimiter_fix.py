from pathlib import Path

path = Path('scripts/tmp_sp001_r3_reader_v2.py')
text = path.read_text(encoding='utf-8')
replacements = [
    (
        "r'\\raggedcolumns' + text[after:].lstrip('\\n')",
        "r'\\raggedcolumns' + '\\n' + text[after:].lstrip('\\n')",
    ),
    (
        "r'\\raggedcolumns' + text[cite_end:].lstrip('\\n')",
        "r'\\raggedcolumns' + '\\n' + text[cite_end:].lstrip('\\n')",
    ),
]
changed = 0
for old, new in replacements:
    count = text.count(old)
    if count:
        text = text.replace(old, new)
        changed += count
if changed != 3:
    raise SystemExit(f'expected 3 raggedcolumns delimiter repairs, got {changed}')
path.write_text(text, encoding='utf-8')
print(f'delimiter repairs applied: {changed}')
