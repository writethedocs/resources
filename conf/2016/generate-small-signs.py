from __future__ import print_function

import os
import sys
import argparse
import xml
import fileinput
from xml.etree.ElementTree import parse, register_namespace, Element

import yaml

def edit_svg_text(document, text=None, output=None):
    if output is None:
        output = sys.stdout
    ns = {
        'svg': 'http://www.w3.org/2000/svg',
        'inkscape': 'http://www.inkscape.org/namespaces/inkscape',
        '': 'http://www.w3.org/2000/svg'
    }
    xpath = './/svg:flowRoot[@id="sign-text"]'
    try:
        for node in document.findall(xpath, ns):
            style = node.get('style')
            style_parts = style.split(';')
            if len(text) > 128:
                style_parts.append('font-size: 28px')
            elif len(text) > 64:
                style_parts.append('font-size: 36px')
            elif len(text) > 32:
                style_parts.append('font-size: 48px')
            node.set('style', ';'.join(style_parts))
            for child in node.findall('svg:flowPara', ns):
                node.remove(child)
            for line in text.split('\n'):
                elem = Element('flowPara')
                elem.text = line
                node.append(elem)
    except TypeError:
        pass
    document.write(output)


if __name__ == '__main__':
    register_namespace('svg', 'http://www.w3.org/2000/svg')
    register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
    register_namespace('cc', 'http://creativecommons.org/ns#')
    register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    register_namespace('xlink', 'http://www.w3.org/1999/xlink')
    register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
    register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')
    register_namespace('', 'http://www.w3.org/2000/svg')

    signs = yaml.load(''.join(fileinput.input()))

    for (sign_name, sign) in signs.items():
        filename = sign.get('file', 'sign-small.svg')
        document = parse(filename)
        output_filename = 'sign-small-{0}.svg'.format(sign_name)
        h = open(output_filename, 'w')
        edit_svg_text(document, text=sign.get('text'), output=h)
