TARGET=paper.pdf
FIGS=

all: $(TARGET)

$(TARGET): $(TARGET:.pdf=.tex) $(FIGS) refs.bib *.tex Makefile
	pdflatex $(TEXFLAGS) $<
	bibtex $(basename $<)
	pdflatex $(TEXFLAGS) $<
	pdflatex $(TEXFLAGS) $<

test: test-fonts test-info

test-fonts: $(TARGET)
	pdffonts $<

test-info: $(TARGET)
	pdfinfo $<

print: $(TARGET)
	pdftops $< - | lpr

view: $(TARGET)
	okular $< &

clean:
	rm -f *.log *.aux *.bbl *.blg *.out paper.pdf *~
