# -*- coding: utf-8 -*-

from enum import Enum, unique

# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#print(Weekday(7))

for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

