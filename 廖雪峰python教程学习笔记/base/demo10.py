# -*- coding: utf-8 -*-
import math
from functools import reduce

def add(x,y,f):
    return f(x) + f(y)

#print(add(-5, 6, abs))

def f(x):
    return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r));

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])));

def add2(x,y):
    return x + y

print(reduce(add2, [1,3,5,7,9]))

#def fn(x,y):
#    return x*10 + y

#print(reduce(fn, [1,3,5,7,9]))

#def char2num(s):
#    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

#print(reduce(fn,map(char2num, '13579')))

def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num, s))

print(str2int('13579'))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name.lower().capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print(L2)

#请编写一个prod()函数，可以接受一个list并利用reduce()求积

def prod(L):
    def quad(x,y):
        return x*y
    return reduce(quad, L)

L3 = [3,5,7,9]

print('3 * 5 * 7 * 9 =', prod(L3))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

L4 = '123.456'
def str2float(s):
    L5 = (L4.split('.'))
    n = len(L5[1])
    def fn(x,y):
        if y == '.':
            return x
        else:
            return x*10 + y
    def char2num2(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':'.'}[s]
    return reduce(fn,map(char2num2, s))*pow(10,-n)

print('str2float(\'123.456\') =', str2float(L4))
