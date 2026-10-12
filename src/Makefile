.PHONY: all verify package clean

all:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex

verify: all
	python3 tools/verify_skeleton.py

package: verify
	python3 tools/package_skeleton.py

clean:
	latexmk -c -outdir=build main.tex
