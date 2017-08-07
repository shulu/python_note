import functools

print(list(map(lambda x: x*x, [1,2,3,4,5,6,7,8,9])))

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def logEn(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__) )
            return func(*args, **kw)
        return wrapper
    return decorator

@logEn('execute')

def now():
    print('2015-3-25')

f= now
f()
print(now.__name__)
print(f.__name__)

now = log(now)

now = logEn('excute')(now)