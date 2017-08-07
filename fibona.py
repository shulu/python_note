def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(10)

def fib2():
    L = [1, 1]
    while True:
        yield L
        L.append( L[-1] + L[-2] )

n = 0
for t in fib2():
    print(t)
    n = n + 1
    if n == 10:
        break
