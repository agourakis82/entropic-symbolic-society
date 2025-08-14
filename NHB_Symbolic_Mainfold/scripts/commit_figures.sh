# Create a helper shell script to copy figures (optional), add, commit and push.
from pathlib import Path
script = """#!/usr/bin/env bash
set -euo pipefail

# commit_figures.sh
# Copies expected figure files into ./figs (optionally from a --from DIR),
# then git-add/commit/push them.
#
# Usage:
#   ./commit_figures.sh
#   ./commit_figures.sh --from /path/to/source
#   ./commit_figures.sh -m "Custom commit message"
#
# Options (order-independent):
#   --from DIR     Copy figures from DIR into ./figs before committing
#   -m "MESSAGE"   Custom commit message
#
# Expected filenames (as referenced by Main_sr.tex):
#   umap_projection.png
#   Fig_symbolic_heatmap.pdf
#   Fig_symbolic_regimes_map.pdf
#   Fig_collapse_recovery.pdf
#   figure2_orc_distribution_and_concept_map_en.png

set +u
SRC_DIR=""
COMMIT_MSG="Add regenerated figures for Main_sr.tex build"
set -u

# Parse args
while [[ $# -gt 0 ]]; do
  case "$1" in
    --from)
      SRC_DIR="$2"; shift 2;;
    -m)
      COMMIT_MSG="$2"; shift 2;;
    *)
      echo "Unknown arg: $1"; exit 2;;
  esac
done

# Ensure we are at repo root (heuristic: check for .git)
if [[ ! -d .git ]]; then
  echo "Error: run this from the root of your git repository ('.git' not found)."
  exit 1
fi

mkdir -p figs

declare -a FILES=(
  "umap_projection.png"
  "Fig_symbolic_heatmap.pdf"
  "Fig_symbolic_regimes_map.pdf"
  "Fig_collapse_recovery.pdf"
  "figure2_orc_distribution_and_concept_map_en.png"
)

# If a source directory was provided, copy files from there (if present)
if [[ -n "${SRC_DIR}" ]]; then
  echo ">> Copying figures from '${SRC_DIR}' to './figs'"
  for f in "${FILES[@]}"; do
    if [[ -f "${SRC_DIR}/${f}" ]]; then
      cp -v "${SRC_DIR}/${f}" "figs/${f}"
    else
      echo "WARN: '${SRC_DIR}/${f}' not found; skipping copy."
    fi
  done
fi

# Verify presence; list missing ones but proceed with existing
MISSING=()
for f in "${FILES[@]}"; do
  if [[ ! -f "figs/${f}" && ! -f "${f}" ]]; then
    MISSING+=("$f")
  fi
done

if (( ${#MISSING[@]} > 0 )); then
  echo "NOTE: The following expected files are missing (will not be committed):"
  for f in "${MISSING[@]}"; do echo "  - $f"; done
fi

# Stage whatever exists among the expected set
TO_ADD=()
for f in "${FILES[@]}"; do
  if [[ -f "figs/${f}" ]]; then
    TO_ADD+=("figs/${f}")
  elif [[ -f "${f}" ]]; then
    TO_ADD+=("${f}")
  fi
done

if (( ${#TO_ADD[@]} == 0 )); then
  echo "Nothing to commit (no expected figure files found)."
  exit 0
fi

echo ">> Staging files:"
printf '  %s\n' "${TO_ADD[@]}"
git add "${TO_ADD[@]}"

# Detect current branch
BRANCH="$(git rev-parse --abbrev-ref HEAD)"
echo ">> Commit on branch: ${BRANCH}"

# Commit
git commit -m "${COMMIT_MSG}" || {
  echo "Commit skipped (no changes)?"
  exit 0
}

# Push
echo ">> Pushing to origin/${BRANCH}"
git push origin "${BRANCH}"

echo "Done."
"""
out = Path("/mnt/data/commit_figures.sh")
out.write_text(script, encoding="utf-8")
import os
os.chmod(out, 0o755)
str(out)
