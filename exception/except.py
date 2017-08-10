# -*- coding: utf-8 -*-
import logging
try:
    print('try..')
    #r = 10/0
    #r = 10/2
    #r = 10 / int('a')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')

print('END')

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)
        print('ERROR:', e)
    finally:
        print('finally')
print('END')
main()