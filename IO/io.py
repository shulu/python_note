# -*- coding: utf-8 -*-

from io import StringIO,BytesIO
import os

f = StringIO()
print(f.write('hello'))
print(f.write('hello!'))
print(f.getvalue())
print(f.write(' '))

ff = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = ff.readline()
    if s == '' :
        break
    print(s.strip())

b = BytesIO()
print(b.write('中文'.encode('utf-8')))
print(b.getvalue())

print(os.name)
#uname在windows中不存在
#print(os.uname())
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.join(os.path.abspath('..')), 'testdir')
#os.mkdir('D:\python_note\dir')
#os.rmdir('D:\python_note\dir')
os.rmdir('D:\python_note\\testdir')