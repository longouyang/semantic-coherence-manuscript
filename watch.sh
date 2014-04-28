while kqwait report.tex images/*
do
latexmk -pdflatex='pdflatex -file-line-error -synctex=1' -pdf report.tex
done
