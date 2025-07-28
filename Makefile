
PDF=main_modular_clean

all: pdf

pdf:
	pdflatex $(PDF).tex
	bibtex $(PDF)
	pdflatex $(PDF).tex
	pdflatex $(PDF).tex

clean:
	rm -f *.aux *.log *.toc *.out *.bbl *.blg *.synctex.gz *.fls *.fdb_latexmk

zip:
	zip -r entropic-symbolic-society.zip * -x '*.aux' '*.log' '*.toc' '*.out' '*.fls' '*.synctex.gz'
