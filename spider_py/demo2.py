#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'


from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry 入队
queue.append("Graham")          # Graham 入队
print(queue.popleft())                 # 队首元素出队
# 输出: 'Eric'
print(queue.popleft())         # 队首元素出队
# 输出: 'John'
print(queue)                           # 队列中剩下的元素
# 输出: deque(['Michael', 'Terry', 'Graham'])

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

print('orange' in basket)

print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)
print(a | b)
print(a&b)
print(a^b)