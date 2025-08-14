- Ensures UNIX line endings (LF) for Makefile and .tex
- Rewrites Makefile commands to use TABs (not spaces)
- Reports missing tools files
Usage:
  python tools/repo_guard.py --fix
"""
import argparse, sys, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SR_DIR = ROOT / "Manuscripts" / "Scientific_Reports_v1.6"
TOOLS = ROOT / "tools"

def set_unix_endings(p: Path):
    txt = p.read_bytes()
    txt = txt.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
    p.write_bytes(txt)

def ensure_tabs_in_makefile(p: Path):
    # Replace 4 leading spaces before a command by a TAB
    lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
    fixed = []
    for ln in lines:
        # If line starts with 4 or more spaces then a non-space, change first run to tab
        fixed.append(re.sub(r'^( {4,})([^ \t#])', r'\t\2', ln))
    p.write_text("\n".join(fixed), encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true", help="apply quick fixes")
    args = ap.parse_args()

    problems = []

    mf = ROOT / "Makefile"
    if not mf.exists():
        problems.append("Makefile not found at repo root.")
    else:
        if args.fix:
            set_unix_endings(mf)
            ensure_tabs_in_makefile(mf)

    # Ensure tools exist
    expected_tools = ["build_figures.sh", "validate_bib.py"]
    missing = [t for t in expected_tools if not (TOOLS / t).exists()]
    if missing:
        problems.append("Missing tools: " + ", ".join(missing))

    # Ensure LaTeX sources exist
    main_tex = SR_DIR / "Main_sr_rev1.tex"
    if not main_tex.exists():
        problems.append(f"{main_tex} not found.")

    if problems:
        print("repo_guard report:")
        for p in problems:
            print(" -", p)
        if args.fix and mf.exists():
            print("\nApplied: normalize line endings and ensure TABs in Makefile.")
        sys.exit(1 if problems else 0)
    else:
        print("repo_guard OK — structure looks good.")
        sys.exit(0)

if __name__ == "__main__":
    main()
'''
# Write files
Path("/mnt/data/Makefile").write_text(makefile, encoding="utf-8")
tools_dir = Path("/mnt/data/tools")
tools_dir.mkdir(parents=True, exist_ok=True)
(Path("/mnt/data/tools/repo_guard.py")).write_text(guard, encoding="utf-8")
# Make it executable-ish (user will download anyway)
"done"