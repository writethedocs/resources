# Write the Docs 2015

These are the image assets for Write the Docs 2015. The SVG files were created
using Inkscape, so some functionality is tied to that implementation. There is a
Makefile in this directory which handles generating files for both EU and NA
conferences from a single SVG.

## Generated Assets

Major assets are generated from a single source SVG. The makefile handles the
output of these files to `na/` and `eu/` output paths for final PDFS and PNGS.
Try to avoid forking these assets for each conference, instead edit the common
sources and generate the assets, if you can.

To generate the assets for WTD NA: `make` or `make CONF=na`

To generate the assets for WTD EU: `make CONF=eu`

To clean out everything and regenerate: `make clean assets`. Note: you'll need
Inkscape and the font installed.

Some of the finer details on keeping a single SVG source for multiple PDF/PNG
outputs:

  * A transform script, `transform-svg.py` uses XPath selectors to hide and show
    selected elements. It takes `--hide=<xpath selector>` and `--show=<xpath
    selector>` as arguments. See the Makefile for implementations.

  * SVG files are split up with Inkscape layers. Common elements are in one
    layer, with a layer for NA and a layer for EU. These are `svg:g` XML
    elements and have the `wtd` attribute.

  * Layers for NA only should have the XML attribute `wtd='na'`

  * Layers for EU only should have the XML attribute `wtd='eu'`

  * The Makefile determines which to show and hide and appends those calls to
    the transform script automatically.

## One-off Assets

Each conference has a few SVG files in the generated `na/` and `eu/` paths.
These can be edited in the `na/` and `eu/` paths without fear of being
overwritten by generated output.

## Information on Assets

Coming soon.
