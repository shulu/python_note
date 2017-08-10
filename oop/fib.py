# -*- coding: utf-8 -*-

class Fib(object):

    def __init__(self):
        self.a, self.b = 0,1

    def __iter__(self):
        return  self

    def __next__(self):
        self.a,self.b = self.b, self.a+self.b
        if self.a > 20:
            raise StopIteration()
        return  self.a

    def __getitem__(self, n):
        a, b = 1,1
        if isinstance(n, int):
            for x in range(n):
                a,b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            L = []
            for x in range(stop):
                if x>= start:
                    L.append(a)
                a, b  = b, a+b
            return L

for n in Fib():
    print(n)

f = Fib()
print(f[0])

print(f[0:5])
print(f[:10])