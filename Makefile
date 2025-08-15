FIGURE_DIRS = \
	Manuscripts/Scientific_Reports_v1.6/figures \
	NHB_Symbolic_Mainfold/code/figs_final \
	NHB_Symbolic_Mainfold/figs \
	figs

FIGURE_TARGET_DIR = Manuscripts/Scientific_Reports_v1.6/figures
MAIN_TEX = Manuscripts/Scientific_Reports_v1.6/Main_sr.tex

.PHONY: pdf figures clean distclean validate

figures:
	mkdir -p $(FIGURE_TARGET_DIR)
	@for dir in $(FIGURE_DIRS); do \
		if [ -d "$$dir" ]; then \
			find "$$dir" -maxdepth 1 -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.pdf' \) -print0 | \
			xargs -0 -I{} cp -u "{}" $(FIGURE_TARGET_DIR) 2>/dev/null || true; \
		fi; \
	done
	@echo "[ok] figures: synced to $(FIGURE_TARGET_DIR)"

pdf: figures
	latexmk -pdf -interaction=nonstopmode -halt-on-error -cd -f $(MAIN_TEX)

clean:
	latexmk -C -cd Manuscripts/Scientific_Reports_v1.6/

distclean: clean
	rm -f $(FIGURE_TARGET_DIR)/*

validate:
	bash tools/validate_bib.sh || true
