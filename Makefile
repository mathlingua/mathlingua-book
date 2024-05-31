
.PHONY: build
build:
	mkdir -p docs && cp -Rf images docs && cp support/styles.css docs && pandoc index.md -o docs/index.html --template=support/template.html --metadata title='Mathlingua' --metadata author='Dominic Kramer' --toc -s --mathjax

.PHONY: dev
dev:
	python3 scripts/dev-server.py
