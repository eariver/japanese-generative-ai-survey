from pathlib import Path

path = Path('scripts/tmp_sp001_r3_reader_v2.py')
text = path.read_text(encoding='utf-8')
replacements = {
    "r'\\\\raggedcolumns' + text[after:].lstrip('\\n')": "r'\\\\raggedcolumns' + '\\n' + text[after:].lstrip('\\n')",
    "r'\\\\raggedcolumns' + text[cite_end:].lstrip('\\n')": "r'\\\\raggedcolumns' + '\\n' + text[cite_end:].lstrip('\\n')",
}
for old, new in replacements.items():
    count = text.count(old)
    if count < 1:
        raise SystemExit(f'expected generator pattern not found: {old}')
    text = text.replace(old, new)
path.write_text(text, encoding='utf-8')
print('delimiter repair applied')
