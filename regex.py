# -*- coding: utf-8 -*-

import re

s = r'ABC\-001'

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

a = 'a b   c'
print(a.split(' '))
print(re.split(r'\s+', a))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

re_email = re.compile(r'^([\d\w\.]+)@([\d\w]+).([a-z]{2,3})$')

print(re_email.match('someone@gmail.com').groups())
print(re_email.match('bill.gates@microsoft.com').groups())
print(re_email.match('sl19911202@microsoft.com').groups())

name = input('please input the name u find: ')
email = input('please inout the email u want find: ')
if re_email.match(email):
    groups = re_email.match(email).groups()
    if name in groups:
        print(email)
else:
    print('not a regular email')