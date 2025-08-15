#!/usr/bin/env python3
# tools/repo_guard.py — normalize EOLs (LF) and fix Makefile TABs.
from pathlib import Path

def fix_makefile_tabs(p: Path):
    if not p.exists(): return
    txt = p.read_text(encoding="utf-8", errors="ignore").splitlines()
    out = []
    for line in txt:
        # Replace 8 leading spaces by a TAB only for recipe lines (heuristic):
        if line.startswith("        "):  # 8 spaces
            out.append("\t" + line[8:])
        else:
            out.append(line)
    p.write_text("\n".join(out) + "\n", encoding="utf-8")

def normalize_lf(p: Path):
    b = p.read_bytes()
    b = b.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    p.write_bytes(b)

def main():
    root = Path(".").resolve()
    # Fix Makefile
    mf = root / "Makefile"
    if mf.exists(): fix_makefile_tabs(mf)
    # Normalize LF for common text files
    exts = {".tex",".bib",".md",".yml",".yaml",".txt",".py",".sh"}
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in exts:
            try: normalize_lf(p)
            except Exception: pass
    print("[ok] repo_guard: normalized LF and Makefile tabs")

if __name__ == "__main__":
    main()
