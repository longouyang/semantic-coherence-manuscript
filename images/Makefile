%.eps: %.pdf
	pdftops -eps "$<" > "$@"

all : $(patsubst %.pdf,%.eps,$(wildcard *.pdf))