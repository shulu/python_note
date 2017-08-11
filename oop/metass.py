# -*- coding: utf-8 -*-

#metaclass是类的模板 所以必须从type类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)

print(L)

def fn(self, name='world'): #定义函数
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
print(h.hello())