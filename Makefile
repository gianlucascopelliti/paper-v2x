ISPELLPAT = -ktexskip1 +cref,Cref,url
SPELLCHECK= chapters/*.tex

SRC_FILES = *.bst *.cls *.sty \
			chapters/* chapters/appendix/* \
			figures/* figures/drawio/* figures/markov-tikzplot/* \
			listings/* tables/* \
			acros.tex \
			header.tex \
			paper.tex \
			bibliography.bib \

all: paper.pdf

graphics:
	${MAKE} -C figures/
	$(MAKE) -C figures/markov-tikzplot
	$(MAKE) -C figures/drawio

paper.pdf: graphics *.bib *.tex chapters/*.tex
	latexmk -pdf paper.tex

demo.pdf: graphics *.bib *.tex chapters/*.tex
	latexmk -pdf demo.tex

spelling: ${SPELLCHECK}
	for file in ${SPELLCHECK}; do \
          ispell -t ${ISPELLPAT} -b -d american -p ./paper.dict $$file; \
        done

zip_src:
	zip src.zip $(SRC_FILES)

clean:
	latexmk -C -pdflatex='pdflatex -file-line-error' -pdf paper.tex
	rm -f paper.pdf
	rm -f *.tex.bak

distclean: clean
	${MAKE} -C figures/ clean
	$(MAKE) -C figures/markov-tikzplot clean
	rm -f paper.bbl

