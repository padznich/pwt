
#1 example - Fibonache
def fib(n):
    a, b = 1, 1
    for i in range(i-1):
        a, b = b, a + b
    return(a)
#import fib   '\n'   fib.fib(10) # 55

#2 examvple
def f2(x, y, *args, **kwargs):
    print('x = {}, y = {}, args = {}, kwargs = {}'.format(x, y, args, kwargs))
    print(type(args))
    print(type(kwargs))
    print('kwargs[\'b\']: ', kwargs['b'])
    print('args[2]: ', args[2])
f2(1, 2, 3, 4, 5, 6, 7, a = 1, b = 2, c =3)

#3 example


