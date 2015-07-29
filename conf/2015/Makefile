# WTD generated output

CONF ?= na

INPUT_FILES = \
	sign-large.svg \
	hoodie.svg \
	sticker.svg \
	tshirt.svg

INPUT_EXTRA_FILES = \
	sign-tall-registration.svg \
	sign-tall-main.svg \
	badge-blank.svg \
	badge-fill.svg \
	badge-example.svg
ifeq ('$(CONF)', 'na')
INPUT_EXTRA_FILES += sign-tall-lolas.svg
endif

INPUT_CONF_FILES = $(addprefix $(CONF)/,$(INPUT_FILES) $(INPUT_EXTRA_FILES))
OUTPUT_FILES = $(foreach file,$(INPUT_CONF_FILES),$(subst svg,pdf,$(file)))

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

asset-pdfs: $(OUTPUT_FILES) $(OUTPUT_EXTRA_FILES)

asset-images: $(CONF)/sticker.png

clean:
	-rm $(INPUT_CONF_FILES)
	-rm $(OUTPUT_FILES)
	-rm $(CONF)/sticker.png

deps:
	[ -d '$(CONF)/' ] || mkdir -p '$(CONF)/'

# Specific rules
.INTERMEDIATE: $(CONF)/sign-tall-registration.svg \
	$(CONF)/sign-tall-main.svg \
	$(CONF)/sign-tall-lolas.svg

$(CONF)/sign-tall-registration.svg: sign-tall.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) \
		--hide './/svg:g[@inkscape:label="Symbols"]/svg:g' \
		--show './/svg:g[@inkscape:label="Symbols"]/svg:g[@inkscape:label="Registration"]' \
		$? > $@

$(CONF)/sign-tall-main.svg: sign-tall.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) \
		--hide './/svg:g[@inkscape:label="Symbols"]/svg:g' \
		--show './/svg:g[@inkscape:label="Symbols"]/svg:g[@inkscape:label="Main"]' \
		$? > $@

$(CONF)/sign-tall-lolas.svg: sign-tall.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) \
		--hide './/svg:g[@inkscape:label="Symbols"]/svg:g' \
		--show './/svg:g[@inkscape:label="Symbols"]/svg:g[@inkscape:label="Lolas"]' \
		$? > $@

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
