# WTD generated output

CONF ?= na

INPUT_FILES = \
	sign-large.svg \
	hoodie.svg

INPUT_EXTRA_FILES = \
	sign-tall-registration.svg \
	sign-tall-main.svg
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
assets: deps $(OUTPUT_FILES) $(OUTPUT_EXTRA_FILES)

clean:
	-rm $(INPUT_CONF_FILES)
	-rm $(OUTPUT_FILES)

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

# General rules
 $(CONF)/%.svg: %.svg
	$(TRANSFORM) $(TRANSFORM_OPTS) $? > $@

$(CONF)/%.pdf: $(CONF)/%.svg
ifndef INKSCAPE
	echo 'Skipping Inkscape PDF generation, install Inkscape for PDF export'
	exit 1
else
	$(INKSCAPE) $(INKSCAPE_OPTS) --file=$? --export-pdf=$@
endif
