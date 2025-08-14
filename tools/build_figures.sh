#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CODE_DIR="$ROOT_DIR/NHB_Symbolic_Mainfold/code"
FIGS_DIR="$CODE_DIR/figs"
FIGS_FINAL_DIR="$CODE_DIR/figs_final"

cd "$ROOT_DIR"

# venv leve
if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r "$ROOT_DIR/NHB_Symbolic_Mainfold/requirements.txt"

mkdir -p "$FIGS_DIR" "$FIGS_FINAL_DIR"

# 1) Gera figuras canônicas com nomes usados no TeX
python "$CODE_DIR/simulate_entropy_curvature.py"      || true
python "$CODE_DIR/simulate_regime_map.py"            || true
python "$CODE_DIR/simulate_collapse_recovery.py"     || true

# 2) Se existir o orc analysis figure, leve para a pasta do manuscrito também
if [[ -f "$ROOT_DIR/Manuscripts/Scientific_Reports_v1.6/figures/figure2_orc_distribution_and_concept_map_en.png" ]]; then
  echo "ORC figure present."
fi

# 3) Cópias para figs_final mantendo os nomes esperados pelo TeX
for base in Fig_symbolic_heatmap Fig_symbolic_regimes_map Fig_collapse_recovery; do
  for ext in png pdf; do
    if [[ -f "$FIGS_DIR/${base}.${ext}" ]]; then
      cp -f "$FIGS_DIR/${base}.${ext}" "$FIGS_FINAL_DIR/${base}.${ext}"
    fi
  done
done

# 4) (Opcional) Também roda aggregator/cópias customizadas se você quiser ED/renomeadas
python "$CODE_DIR/make_figures.py" || true

echo "Figures built/copied to:"
echo " - $FIGS_DIR"
echo " - $FIGS_FINAL_DIR"
