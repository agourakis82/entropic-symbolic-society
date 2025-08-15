#!/usr/bin/env python3
"""
Bibliography validator: compare citation keys in a LaTeX file against .bib entries.
Usage:
  python tools/validate_bib.py --tex Manuscripts/Scientific_Reports_v1.6/Main_sr.tex --bib Manuscripts/Scientific_Reports_v1.6/refs.bib
Exit code: 0 OK, 1 missing keys, 2 I/O error.
"""
import re, sys, argparse
from pathlib import Path

CITE_RE = re.compile(r"\\cite[a-zA-Z]*\s*\{([^}]+)\}")

def parse_tex_keys(texpath: Path):
    text = texpath.read_text(encoding="utf-8", errors="ignore")
    keys = set()
    for m in CITE_RE.finditer(text):
        for k in m.group(1).split(","):
            k = k.strip()
            if k:
                keys.add(k)
    return keys

def parse_bib_keys(bibpath: Path):
    text = bibpath.read_text(encoding="utf-8", errors="ignore")
    bib_re = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")
    return set(bib_re.findall(text))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tex", required=True)
    ap.add_argument("--bib", required=True)
    args = ap.parse_args()
    tex = Path(args.tex); bib = Path(args.bib)
    if not tex.exists() or not bib.exists():
        print(f"[error] missing file(s): tex={tex.exists()} bib={bib.exists()}", file=sys.stderr)
        return 2
    used = parse_tex_keys(tex)
    present = parse_bib_keys(bib)
    missing = sorted(used - present)
    unused = sorted(present - used)
    print(f"[info] citations in TEX: {len(used)}")
    print(f"[info] entries in BIB:  {len(present)}")
    if missing:
        print("\n[missing] cited in TEX but absent in BIB:")
        for k in missing: print("  -", k)
    if unused:
        print("\n[unused] in BIB but not cited in TEX:")
        for k in unused: print("  -", k)
    return 1 if missing else 0

if __name__ == "__main__":
    sys.exit(main())
