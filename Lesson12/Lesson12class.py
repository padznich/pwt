# coding=utf-8

import os
import sys
#
print(sys.path)
#
print(os.getcwdu())
#
#
'''
x = 1
def f():
    x = 2
    print("in f, x={}".format(x))
f()
print("globally, x={}".format(x))
'''
#
'''
x = 1
def g():
    def f():
        print("in f, x={}".format(x))
    x = 3
    print("in g, x={}".format(x))
    f()
g()
print("globally, x={}".format(x))
'''
#
'''
x = 1
def f():
    global x
    x = 2
    print("in f, x={}".format(x))
f()
print("globally, x={}".format(x))
'''
#
'''
def f():
    id = 1
    print("in f, id={}".format(id))
f()
print("globally, id={}".format(id))
'''
print(sys.modules)
