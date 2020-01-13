PDFLATEX := pdflatex -interaction=nonstopmode -halt-on-error
LCC := latexmk
BUILD := se-scientific-affinity-paper
DIFF := se-scientific-affinity-paper_v1_v2
.PHONY: all clean

all: $(BUILD).pdf $(DIFF).pdf

$(DIFF).pdf: $(DIFF).tex
	$(LCC) -bibtex -pdf -pdflatex="$(PDFLATEX)" -use-make $(DIFF).tex

$(BUILD).pdf: $(BUILD).tex
	$(LCC) -bibtex -pdf -pdflatex="$(PDFLATEX)" -use-make $(BUILD).tex

clean:
	$(LCC) -bibtex -CA

cleanaux:
	$(LCC) -bibtex -c
