# -*- coding: utf-8 -*-
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1,2,4,5,6,9,10,15])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))


#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
def is_palindrome(n):
    m = str(n)
    m = m[::-1]
    m = int(m)
    if n>10 and n==m:
        return n

#output = is_palindrome(11)
output = list(filter(is_palindrome ,range(1,1000)))
print(output)
