# coding=utf-8
'''
import collections

Point = collections.namedtuple('Point', ['y', 'x'])
p = Point(x=1, y=2)

print(p)

print(p[0], p[1])
print(p.x, p.y)
'''

class A(object):

    a = 1

    def __init__(self):
        self.b = 2

    def f1(self):
        self.c = 3

class B(A):

    def add(self, val):
        self.__class__.__self__.b = self.b + val

a = B()
print(a.b)
a.add(6)
print(a.b)


