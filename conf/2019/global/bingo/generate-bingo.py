# from __future__ import print_function

import sys
import argparse
import xml
import random
from xml.etree.ElementTree import parse, register_namespace, Element


PHRASE_STRING = """Ask a speaker a question
Introduce yourself to someone new
Talk to one of the sponsors
Go to the opening reception
Join a group conversation 
Tweet about a talk
Decorate your name tag
Attend an unconference session
Grab dinner with another WTD attendee
Thank a volunteer
Show someone your bingo card
Have some quiet time in Lola's room
Say hello in the WTD slack channel
Add a new connection on LinkedIn
Check out the job fair
Attend the Welcome Wagon tour
Grab a snack
Take a break
Brainstorm a lightning talk for next year
Talk to your neighbor between talks
Leave a spot for someone to join your group
Drink some water
Relax at the Monday night social event
Go to the Writing Day
Register and get your badge"""

PHRASES = PHRASE_STRING.split('\n')

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
