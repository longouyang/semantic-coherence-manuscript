reference-titles.txt: references.bib
	python get-bibtex-titles.py "$<" > "$@"

search-dois.sh: reference-titles.txt
	node make-crossref-links.js "$<" > "$@"

with-dois.bib : references.bib search-dois.csv
	python inject-dois.py references.bib search-dois.csv > "$@"

clean:
	rm reference-titles.txt search-doi.sh

report.pdf : report.tex images/*
	latexmk -pdflatex='pdflatex -file-line-error -synctex=1 -interaction=nonstopmode' -pdf report.tex;

all : with-dois.bib report.pdf
