# -*- coding: utf-8 -*-
import re
import base64
from xml.parsers.expat import ParserCreate

def safe_base64_decode(s):
    if isinstance(s, bytes):
        s = s.decode('utf-8')
    b = len(s) % 4
    if b > 0:
        return base64.b64decode(s+'='*(4-b))
    else:
        return base64.b64decode(s)

#s = base64.b64decode('abcd')
#print(s)
#ss = base64.b64decode(b'YWJjZA==')
#print(ss)
#ss = base64.b64decode(b'YWJjZA')
#print(ss)
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

