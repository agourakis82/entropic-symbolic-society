#!/usr/bin/env python3
import re, sys, argparse
from pathlib import Path

CITE_KEY_RE = re.compile(r'\\cite[tp]?\\*?\\?\\{([^}]+)\\}')
ENTRY_RE    = re.compile(r'^@\\w+\\{\\s*([^,\\s]+)\\s*,', re.I | re.M)
DOI_RE      = re.compile(r'\\b10\\.\\d{4,9}/[-._;()/:A-Z0-9]+\\b', re.I)

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tex', required=True)
    ap.add_argument('--bib', required=True)
    return ap.parse_args()

def cited_keys(tex_text:str) -> set[str]:
    keys = set()
    for m in CITE_KEY_RE.finditer(tex_text):
        for k in m.group(1).split(','):
            keys.add(k.strip())
    return keys

def bib_keys(bib_text:str) -> set[str]:
    return set(m.group(1).strip() for m in ENTRY_RE.finditer(bib_text))

def find_bad_fields(bib_text:str) -> list[tuple[int,str]]:
    issues=[]
    for i, line in enumerate(bib_text.splitlines(), start=1):
        if line.strip().lower().startswith('file ='):
            issues.append((i, 'local file field should be removed'))
        if 'doi =' in line.lower():
            if not DOI_RE.search(line):
                issues.append((i, 'malformed DOI'))
    return issues

def main():
    args = parse_args()
    tex = Path(args.tex).read_text(encoding='utf-8', errors='ignore')
    bib = Path(args.bib).read_text(encoding='utf-8', errors='ignore')

    used = cited_keys(tex)
    present = bib_keys(bib)

    missing = sorted(used - present)
    unused  = sorted(present - used)

    print('=== Bibliography validation (dry-run) ===')
    print(f'Cited keys in TEX: {len(used)}')
    print(f'Entries in BIB:   {len(present)}')
    if missing:
        print('\\n!! Missing entries (cited in TEX but absent in BIB):')
        for k in missing: print(f'  - {k}')
    else:
        print('\\nOK: no missing entries.')

    if unused:
        print('\\n-- Unused entries (present in BIB but not cited):')
        for k in unused: print(f'  - {k}')
    else:
        print('\\nOK: no unused entries.')

    issues = find_bad_fields(bib)
    if issues:
        print('\\n!! Suspicious fields in BIB:')
        for ln,msg in issues:
            print(f'  line {ln}: {msg}')
    else:
        print('\\nOK: no suspicious fields detected.')

if __name__ == '__main__':
    main()
