
.PHONY: build
build:
	mkdir -p docs && cp -Rf images docs && cp styles.css docs && pandoc index.md -o docs/index.html --template=template.html --metadata title='Mathlingua' --metadata author='Dominic Kramer' --toc -s --mathjax
