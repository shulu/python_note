# -*- coding: utf-8 -*-

def triangles():
    L=[1]
    while True:
        yield L
        L = [1] + [ L[x-1] + L[x] for x in range(1,len(L)) ] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
