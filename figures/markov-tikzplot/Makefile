all: small-tikz.pdf


small-tikz.pdf: *.tex
	latexmk -pdf small-tikz.tex
	pdfcrop small-tikz.pdf small-tikz.pdf

clean:
	latexmk -C -pdflatex='pdflatex -file-line-error' -pdf small-tikz.tex
	rm -f small-tikz.pdf
	rm -f *.tex.bak

