while kqwait report.tex figures/*
do
latexmk -pdflatex='pdflatex -file-line-error -synctex=1' -pdf report.tex
done
