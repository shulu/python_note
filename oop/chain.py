# -*- coding: utf-8 -*-

class Chain(object):

    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s / %s' % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__

    def __call__(self, path):
        return Chain('%s / %s' % (self.__path, path))

print(Chain().status.user.timeline.list)
print(Chain().users('will').repos)