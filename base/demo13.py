def cal_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print(cal_sum(1,2,3,4,65))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,65)
print(f)
print(f())

def count():
    fs = []
    for i in range(1,4):
        print(i)
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for x in range(1,4):
        fs.append(f(x))
    return fs

f4, f5, f6 = count()

print(f4())
print(f5())
print(f6())











