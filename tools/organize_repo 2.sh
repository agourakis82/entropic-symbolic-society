#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

SR_DIR="$ROOT_DIR/Manuscripts/Scientific_Reports_v1.6"
CODE_DIR="$ROOT_DIR/NHB_Symbolic_Mainfold/code"
FIGS_DIR="$CODE_DIR/figs"
FIGS_FINAL_DIR="$CODE_DIR/figs_final"

echo ">>> Ensuring directory layout"
mkdir -p "$FIGS_DIR" "$FIGS_FINAL_DIR" "$SR_DIR/figures" "$ROOT_DIR/tools"

echo ">>> Ensure jabbrv files are visible to SR build"
# Copia apenas se não existirem no diretório do manuscrito
for f in "$ROOT_DIR/jabbrv.sty" "$ROOT_DIR/jabbrv-ltwa-all.ldf" "$ROOT_DIR/jabbrv-ltwa-en.ldf"; do
  if [[ -f "$f" ]]; then
    base=$(basename "$f")
    if [[ ! -f "$SR_DIR/$base" ]]; then
      cp -n "$f" "$SR_DIR/$base"
    fi
  fi
done

echo ">>> Patching LaTeX: natbib + graphicspath"
# Ajusta \usepackage{cite} -> natbib e \graphicspath nos dois .tex (se existirem)
for TEX in "$SR_DIR/Main_sr_rev1.tex" "$SR_DIR/Main_sr.tex"; do
  [[ -f "$TEX" ]] || continue

  # 1) Troca cite por natbib (se cite estiver presente)
  if grep -q '\\usepackage{cite}' "$TEX"; then
    perl -0777 -pe 's/\\usepackage\{cite\}/\\usepackage[numbers,sort&compress]{natbib}/' -i "$TEX"
  fi
  # 2) Garante float (para opção [H]) — só adiciona se não existir
  if ! grep -q '\\usepackage{float}' "$TEX"; then
    perl -0777 -pe 's/(\\usepackage\{.*graphicx.*\}\s*)/\1\n\\usepackage{float}\n/s' -i "$TEX"
  fi
  # 3) Ajusta \graphicspath para incluir figs/ e figures/
  perl -0777 -pe 's/\\graphicspath\{[^\}]*\}/\\graphicspath{{NHB_Symbolic_Mainfold\/code\/figs_final\/}{NHB_Symbolic_Mainfold\/code\/figs\/}{Manuscripts\/Scientific_Reports_v1.6\/figures\/}{.\/}}/s' -i "$TEX"
done

echo ">>> (Optional) Running figure build"
"$ROOT_DIR/tools/build_figures.sh" || true

echo ">>> Validating bibliography"
python3 "$ROOT_DIR/tools/validate_bib.py" \
  --tex "$SR_DIR/Main_sr_rev1.tex" \
  --bib "$SR_DIR/refs.bib" || true

echo ">>> Done. You can now compile from $SR_DIR:"
echo "     latexmk -pdf -interaction=nonstopmode Main_sr_rev1.tex"
