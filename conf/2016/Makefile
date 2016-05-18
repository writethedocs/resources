# WTD generated output

CONF ?= na

INPUT_FILES = \
	sign-large.svg \
	hoodie.svg \
	sticker.svg \
	tshirt.svg \
	bookmark.svg

BINGO_CARDS = $(addsuffix .svg,$(addprefix bingo-card-,0 1 2 3 4 5 6 7 8 9))
BINGO_CARDS_OUTPUT = $(foreach file,$(BINGO_CARDS),$(subst svg,pdf,$(file)))

INPUT_EXTRA_FILES = \
	sign-tall.svg \
	badge-blank.svg \
	badge-fill.svg \
	badge-example.svg \
	notebook.svg \
	$(BINGO_CARDS)

INPUT_CONF_FILES = $(addprefix $(CONF)/,$(INPUT_FILES) $(INPUT_EXTRA_FILES))
OUTPUT_FILES = $(foreach file,$(INPUT_CONF_FILES),$(subst svg,pdf,$(file)))
OUTPUT_EXTRA_FILES = \
	notebook-foreground.pdf \
	notebook-background.pdf \
	notebook-combined.pdf

SIGNS = $(shell python -c "import yaml; objs = yaml.load(open('signs.yaml')); print(' '.join(objs.keys()))")
SIGN_FILES = $(addprefix sign-small-,$(addsuffix .svg, $(SIGNS)))
SIGN_OUTPUT_FILES = $(addprefix $(CONF)/,$(SIGN_FILES))

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
assets: deps asset-pdfs asset-images assets-signs asset-bingo

asset-pdfs: $(OUTPUT_FILES) $(OUTPUT_EXTRA_FILES)

asset-images: $(CONF)/sticker.png

asset-signs: $(foreach file,$(SIGN_OUTPUT_FILES),$(subst svg,pdf,$(file)))

asset-bingo: $(foreach file,$(addprefix $(CONF)/,$(BINGO_CARDS)),$(subst svg,pdf,$(file)))

clean:
	-rm $(INPUT_CONF_FILES)
	-rm $(OUTPUT_FILES)
	-rm $(CONF)/sticker.png

deps:
	[ -d '$(CONF)/' ] || mkdir -p '$(CONF)/'

# Signs
.INTERMEDIATE: $(CONF)/sign-tall.svg \
	$(SIGN_OUTPUT_FILES) \
	$(SIGN_FILES)

$(CONF)/sign-small-%.svg: sign-small-%.svg
	mv $? $@

$(SIGN_FILES): sign-small.svg sign-handout.svg signs.yaml
	python generate-small-signs.py

# Badge
.INTERMEDIATE: $(CONF)/badge-blank.svg \
	$(CONF)/badge-fill.svg \
	$(CONF)/badge-example.svg

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

# Notebook
.INTERMEDIATE: $(CONF)/notebook-foreground.svg \
	$(CONF)/notebook-background.svg \
	$(CONF)/notebook-combined.svg

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
.INTERMEDIATE: $(BINGO_CARDS)

$(BINGO_CARDS): bingo.svg
	python generate-bingo.py > $@

# General rules
 $(CONF)/%.svg: %.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) $? > $@

# Image output
$(CONF)/%.png: $(CONF)/%.svg
ifndef INKSCAPE
	echo 'Skipping Inkscape PNG generation, install Inkscape for PNG export'
	exit 1
else
	$(INKSCAPE) $(INKSCAPE_OPTS) --export-dpi=600 --file=$? --export-png=$@
endif

# PDF output
$(CONF)/%.pdf: $(CONF)/%.svg
ifndef INKSCAPE
	echo 'Skipping Inkscape PDF generation, install Inkscape for PDF export'
	exit 1
else
	$(INKSCAPE) $(INKSCAPE_OPTS) --file=$? --export-pdf=$@
endif
