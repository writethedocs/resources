from __future__ import print_function

import sys
import argparse
import xml
import random
from xml.etree.ElementTree import parse, register_namespace, Element


PHRASES = [
    'Ask a speaker a question',
    'Introduce yourself to someone new',
    'Talk to someone from Google',
    'Join a group conversation',
    'Tweet about a talk',
    'Meet a Github rep',
    'Attend an unconference session',
    'Mingle with WTD folks outside the venue',
    'Thank a volunteer or organizer',
    'Exercise with WTD folks (run/hike/walk)',
    'Chat with a Mozilla developer',
    'Take a Lola\'s room break',
    'Say hello in the WTD slack channel',
    'Give your business card to someone',
    'Wear a piece of swag',
    'Attend the Welcome Wagon tour',
    'Grab a snack',
    'Attend the conference opening party',
    'Brainstorm a lightning talk for next year',
    'Talk to a neighbor',
    'Leave a spot in your group for someone to join',
    'Drink water',
    'Relax at the Monday night party',
    'Go to Writing Day',
]


def replace_text(document, output=None):
    if output is None:
        output = sys.stdout
    ns = {
        'svg': 'http://www.w3.org/2000/svg',
        'inkscape': 'http://www.inkscape.org/namespaces/inkscape',
        '': 'http://www.w3.org/2000/svg'
    }
    xpath = './/svg:flowPara[@class="bingo-text"]'
    phrases = PHRASES
    random.shuffle(phrases)
    try:
        for node in document.findall(xpath, ns):
            node.text = phrases.pop()
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

    document = parse('bingo.svg')
    replace_text(document)
