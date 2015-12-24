# coding=utf-8


'''
class Duck(object):
    fg = 19
    def __init__(self, name):
        self.name = name
    def say(self, msg):
        print("{} said: {}".format(self.name, msg))

class ColorfulDuck(Duck):
    def r(self):
        print(self.__class__.__name__)
    def __init__(self, name, color=None):
        super(ColorfulDuck, self).__init__(name)
        self.color = color
    def say(self, msg):
        # do not say anything
        print("{} with color {} said: {}".format(self.name, self.color, msg))

class D(ColorfulDuck):
    pass

myduck = Duck(name='Rob')
print(myduck.name)
myduck.say('I want sigarets!')

yourdauck = D(name='Wisly')
yourdauck.r()

print(help(yourdauck))
'''

'''
class A(object):
    pass
class B(A):
    pass
class C(B):
    pass

if __name__ == "__main__":
    object_list = (A(), B(), C())
    class_list = (A, B, C)
    for o in object_list:
        for c in class_list:
            print("Class: {}, Object: {}, isinstance: {}".format(c, o, isinstance(o, c)))
    print(class_list)
    print(object_list)
'''

'''
class SmallStupidList(object):
    MAX_LEN = 3
    def __init__(self, *args):
        if len(args) > self.MAX_LEN:
            raise Exception("Too long list")
        self._internal_list = []
        self._internal_list.extend(args)

    def __str__(self):
        return str(self._internal_list)

    def append(self, x):
        if len(self._internal_list) + 1 > self.MAX_LEN:
            raise Exception("Too long list")
        self._internal_list.append(x)
'''