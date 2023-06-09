
.PHONY: serve
serve:
	mdbook serve --dest-dir docs

.PHONY: build
build:
	mdbook build --dest-dir docs

.PHONY: watch
watch:
	mdbook watch --dest-dir docs

.PHONY: clean
clean:
	mdbook clean --dest-dir docs
