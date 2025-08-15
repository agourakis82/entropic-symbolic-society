#!/usr/bin/env bash
set -euo pipefail
TARGET="Manuscripts/Scientific_Reports_v1.6/figures"
mkdir -p "$TARGET"
sync_from() {
  local SRC="$1"
  [ -d "$SRC" ] || return 0
  find "$SRC" -maxdepth 1 -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.pdf' \) -print0 \
  | xargs -0 -I{} cp -u "{}" "$TARGET" 2>/dev/null || true
}
sync_from "Manuscripts/Scientific_Reports_v1.6/figures"
sync_from "NHB_Symbolic_Mainfold/code/figs_final"
sync_from "NHB_Symbolic_Mainfold/figs"
sync_from "figs"
echo "[ok] build_figures: synced into $TARGET"
