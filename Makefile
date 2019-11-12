.PHONY: all clean package cleanaux

all:
	make -C paper
	make -C presentation

clean:
	make -C paper clean
	make -C presentation clean
	rm -rf se-scientific.tar.gz

cleanaux:
	make -C paper cleanaux
	make -C presentation cleanaux

package: all cleanaux
	tar -czf se-scientific.tar.gz presentation/ paper/