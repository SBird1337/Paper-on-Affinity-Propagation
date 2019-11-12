PDFLATEX := pdflatex -interaction=nonstopmode -halt-on-error
LCC := latexmk
BUILD := se-scientific-affinity-paper
.PHONY: all clean

all: $(BUILD).pdf

$(BUILD).pdf: $(BUILD).tex
	$(LCC) -bibtex -pdf -pdflatex="$(PDFLATEX)" -use-make $(BUILD).tex

clean: 
	$(LCC) -bibtex -CA

cleanaux:
	$(LCC) -bibtex -c