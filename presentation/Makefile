PDFLATEX := pdflatex -interaction=nonstopmode -halt-on-error
LCC := latexmk
BUILD := se-scientific-affinity-pres
.PHONY: all clean

all: $(BUILD).pdf

$(BUILD).pdf: $(BUILD).tex
	$(LCC) -pdf -bibtex -pdflatex="$(PDFLATEX)" -use-make $(BUILD).tex

clean: 
	$(LCC) -bibtex -CA

cleanaux:
	$(LCC) -bibtex -c