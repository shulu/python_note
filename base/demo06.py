# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    x = math.sqrt(b**2-(4*a*c))
    x1 = -b + x;
    x1 = x1/(2*a)
    x2 = -b - x;
    x2 = x2/(2*a)
    print(x1,x2)

quadratic(2, 3, 1)