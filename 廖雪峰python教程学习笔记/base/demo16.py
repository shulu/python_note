import functools

def int2 (x, base=2):
    print(int(x, base))

int3 = functools.partial(int, base=2)

print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))

int2('1000000')
int2('1010101')

print(int3('1000000'))
print(int3('1010101'))

print(int3('1000000', base=10))