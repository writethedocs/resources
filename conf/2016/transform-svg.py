from __future__ import print_function

import sys
import argparse
from xml.etree.ElementTree import parse, register_namespace


def transform_svg(document, hide=None, show=None):
    ns = {
        'svg': 'http://www.w3.org/2000/svg',
        'inkscape': 'http://www.inkscape.org/namespaces/inkscape',
        '': 'http://www.w3.org/2000/svg'
    }
    try:
        for xpath in hide:
            for node in document.findall(xpath, ns):
                print('Found node:', xpath, file=sys.stderr)
                node.set('style', 'display:none;')
    except TypeError:
        pass
    try:
        for xpath in show:
            for node in document.findall(xpath, ns):
                print('Found node:', xpath, file=sys.stderr)
                node.set('style', 'display:inline;')
    except TypeError:
        pass
    document.write(sys.stdout)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SVG transform')
    parser.add_argument('--show', action='append')
    parser.add_argument('--hide', action='append')
    parser.add_argument('filename')
    args = parser.parse_args()

    register_namespace('svg', 'http://www.w3.org/2000/svg')
    register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
    register_namespace('cc', 'http://creativecommons.org/ns#')
    register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    register_namespace('xlink', 'http://www.w3.org/1999/xlink')
    register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
    register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')
    register_namespace('', 'http://www.w3.org/2000/svg')

    document = parse(args.filename)
    transform_svg(document, args.hide, args.show)
