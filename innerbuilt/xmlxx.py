# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):

    def start_ele(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_ele(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_ele
parser.EndElementHandler = handler.end_ele
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)