# WTD generated output

CONF ?= na

# Files that go straight to output files, no layer manipulation to create
# multiple files
INPUT_FILES = \
	sign-tall.svg \
	hoodie.svg \
	sticker.svg \
	tshirt.svg \
	bookmark.svg \
	slide-title.svg

SMALL_SIGNS = $(shell python -c "import yaml; objs = yaml.load(open('$(CONF)/signs.yaml')); print(' '.join(objs.keys()))")

ifeq "$(CONF)" "eu"
INPUT_FILES += sign-tall-eu.svg
endif

SMALL_SIGNS_FILES = $(addprefix sign-small-,$(addsuffix .svg, $(SMALL_SIGNS)))
LARGE_SIGNS_FILES = \
	sign-large-banner.svg \
	sign-large-stage.svg
SIGN_FILES = $(SMALL_SIGNS_FILES) $(LARGE_SIGNS_FILES)

BADGE_FILES = \
	badge-blank.svg \
	badge-fill.svg \
	badge-example.svg

NOTEBOOK_FILES = \
	notebook-foreground.svg \
	notebook-background.svg \
	notebook-combined.svg

BINGO_FILES = $(addsuffix .svg,$(addprefix bingo-card-,0 1 2 3 4 5 6 7 8 9))

INPUT_GENERATED_FILES = \
	$(BADGE_FILES) \
	$(SIGN_FILES) \
	$(NOTEBOOK_FILES)

INPUT_CONF_FILES = $(addprefix $(CONF)/,$(INPUT_FILES) $(INPUT_GENERATED_FILES))
OUTPUT_FILES = \
	$(foreach file,$(INPUT_CONF_FILES),$(subst svg,pdf,$(file))) \
	$(CONF)/bingo.pdf

OUTPUT_IMAGE_FILES = \
	$(CONF)/badge.png \
	$(CONF)/notebook.png \
	$(CONF)/tshirt.png \
	$(CONF)/hoodie.png \
	$(CONF)/sticker.png \
	$(CONF)/email-logo.png \
	$(CONF)/site-logo.png

# Commands
INKSCAPE := $(shell which inkscape)
INKSCAPE_OPTS = --export-text-to-path -z

TRANSFORM = python transform-svg.py
ifeq ('$(CONF)', 'na')
TRANSFORM_OPTS = \
	--show './/svg:g[@wtd="na"]' \
	--hide './/svg:g[@wtd="eu"]'
else ifeq ('$(CONF)', 'eu')
TRANSFORM_OPTS = \
	--show './/svg:g[@wtd="eu"]' \
	--hide './/svg:g[@wtd="na"]'
endif

# Rules
assets: deps asset-pdfs asset-images

asset-pdfs: $(OUTPUT_FILES)

asset-images: $(OUTPUT_IMAGE_FILES)

clean:
	-rm $(INPUT_CONF_FILES)
	-rm $(OUTPUT_FILES)
	-rm $(CONF)/sticker.png

deps:
	[ -d '$(CONF)/' ] || mkdir -p '$(CONF)/'

# Signs
.INTERMEDIATE: $(CONF)/sign-tall.svg \
	$(CONF)/sign-large-banner.svg \
	$(CONF)/sign-large-stage.svg \
	$(SIGN_FILES)

$(CONF)/sign-small-%.svg: sign-small-%.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) $? > $@
	rm $?

$(SIGN_FILES): sign-small.svg sign-handout.svg $(CONF)/signs.yaml
	python generate-small-signs.py $(CONF)/signs.yaml

# Large signs
$(CONF)/sign-large-stage.svg: sign-large.svg
ifeq ('$(CONF)', 'na')
	$(eval CONF_SHOW = NA)
	$(eval CONF_HIDE = EU)
else
	$(eval CONF_SHOW = EU)
	$(eval CONF_HIDE = NA)
endif
	$(TRANSFORM) \
		--hide './/svg:g[@inkscape:label="$(CONF_HIDE)"]' \
		--show './/svg:g[@inkscape:label="$(CONF_SHOW)"]' \
		--show './/svg:g[@inkscape:label="$(CONF_SHOW) Sponsors"]' \
		--hide './/svg:g[@inkscape:label="$(CONF_SHOW) Date"]' \
		$? > $@

$(CONF)/sign-large-banner.svg: sign-large.svg
ifeq ('$(CONF)', 'na')
	$(eval CONF_SHOW = NA)
	$(eval CONF_HIDE = EU)
else
	$(eval CONF_SHOW = EU)
	$(eval CONF_HIDE = NA)
endif
	$(TRANSFORM) \
		--hide './/svg:g[@inkscape:label="$(CONF_HIDE)"]' \
		--show './/svg:g[@inkscape:label="$(CONF_SHOW)"]' \
		--hide './/svg:g[@inkscape:label="$(CONF_SHOW) Sponsors"]' \
		--show './/svg:g[@inkscape:label="$(CONF_SHOW) Date"]' \
		$? > $@

# Badge
.INTERMEDIATE: $(addprefix $(CONF)/, $(BADGE_FILES))

$(CONF)/badge-blank.svg: badge.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) \
		--hide './/svg:g[@inkscape:label="Example"]' \
		--hide './/svg:g[@inkscape:label="Fill"]' \
		$? > $@

$(CONF)/badge-fill.svg: badge.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) \
		--hide './/svg:g[@inkscape:label="Example"]' \
		--show './/svg:g[@inkscape:label="Fill"]' \
		$? > $@

$(CONF)/badge-example.svg: badge.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) \
		--hide './/svg:g[@inkscape:label="Fill"]' \
		--show './/svg:g[@inkscape:label="Example"]' \
		$? > $@

# Sticker
.INTERMEDIATE: $(CONF)/sticker.svg

$(CONF)/sticker.png: $(CONF)/sticker.svg
ifndef INKSCAPE
	echo 'Skipping Inkscape PNG generation, install Inkscape for PNG export'
	exit 1
else
	$(INKSCAPE) $(INKSCAPE_OPTS) --export-dpi=600 --file=$? --export-png=$@
endif

# Notebook
.INTERMEDIATE: $(addprefix $(CONF)/, $(NOTEBOOK_FILES))

$(CONF)/notebook-foreground.svg: notebook.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) \
		--hide './/svg:g[@inkscape:label="Guides"]' \
		--hide './/svg:g[@inkscape:label="Background"]' \
		--show './/svg:g[@inkscape:label="Foreground"]' \
		$? > $@

$(CONF)/notebook-background.svg: notebook.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) \
		--hide './/svg:g[@inkscape:label="Guides"]' \
		--hide './/svg:g[@inkscape:label="Foreground"]' \
		--show './/svg:g[@inkscape:label="Background"]' \
		$? > $@

$(CONF)/notebook-combined.svg: notebook.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) \
		--hide './/svg:g[@inkscape:label="Guides"]' \
		--show './/svg:g[@inkscape:label="Foreground"]' \
		--show './/svg:g[@inkscape:label="Background"]' \
		$? > $@

# Bingo
BINGO_PDF_FILES = $(foreach file,$(addprefix $(CONF)/,$(BINGO_FILES)),$(subst svg,pdf,$(file)))

.INTERMEDIATE: $(BINGO_FILES) $(BINGO_PDF_FILES)

$(BINGO_FILES): bingo.svg generate-bingo.py
	python generate-bingo.py > $@

# This isn't important, just cleaner than having 10 similar files laying around
$(CONF)/bingo.pdf: $(BINGO_PDF_FILES)
	@echo ""
	@echo "ACHTUNG!"
	@echo "You'll need to combine the bingo card PDF files into a single file"
	@echo "manually. You can do this with OSX preview and I'm sure other tools."
	@echo ""
	cat $? > $@

# General rules
$(CONF)/%.svg: %.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) $? > $@

# Image output
$(CONF)/%.png: $(CONF)/%.svg
ifndef INKSCAPE
	echo 'Skipping Inkscape PNG generation, install Inkscape for PNG export'
	exit 1
else
	$(INKSCAPE) $(INKSCAPE_OPTS) --export-dpi=90 --file=$? --export-png=$@
endif

# PDF output
$(CONF)/%.pdf: $(CONF)/%.svg
ifndef INKSCAPE
	echo 'Skipping Inkscape PDF generation, install Inkscape for PDF export'
	exit 1
else
	$(INKSCAPE) $(INKSCAPE_OPTS) --file=$? --export-pdf=$@
endif
