# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

ln = [36,5,-12,9,-21]

print(sorted(ln, key=abs))
#sorted里面的key函数是将参数里面的每一个元素放到函数中处理
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
#print(by_name(L));
L2 = sorted(L,key=by_name)
print(L2)
L3 = sorted(L,key = by_score, reverse=True)
print(L3)