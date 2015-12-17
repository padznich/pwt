#http://www.exlab.net/files/tools/sheets/regexp/regexp.pdf

#
# list <=> tuple
#


#
# collections.deque
#
'''
import collections as c
dq = c.deque([1,2,3])
print(dq)

dq.append(4)
dq.appendleft(0)
print(dq)

dq.rotate()
print(dq)

for e in dq:
    print(e)
'''


#
# enumerate
#
'''
list1 = [1 , '2', 3, 4, 5, 6]

f = enumerate(list1)
for i, elem in f:
    print(i, elem)
print(f)
'''


#
# benchmark with datetime
#
'''
import datetime

l = range(10**6)
s = set(range(10**6))
number = 1000

# find in set
start1 = datetime.datetime.now()
for _ in xrange(number):
    10**7 in s
finish1 = datetime.datetime.now()

# find in list
start2 = datetime.datetime.now()
for _ in xrange(number):
    10**7 in l
finish2 = datetime.datetime.now()

print(type(s), "Set time: {}".format(finish1-start1))
print(type(l), "List time: {}".format(finish2-start2))
'''


#
# timeit
#
'''
import timeit
print('_________________list')
print(timeit.timeit(stmt="10**7 in l", setup="l = range(10**6)", number=10))
print(timeit.timeit(stmt="10**7 in l", setup="l = range(10**6)", number=100))
print(timeit.timeit(stmt="10**7 in l", setup="l = range(10**6)", number=1000))

print('_________________set')
print(timeit.timeit(stmt="10**7 in s", setup="s = set(range(10**6))", number=1000))
print(timeit.timeit(stmt="10**7 in s", setup="s = set(range(10**6))", number=10000))
print(timeit.timeit(stmt="10**7 in s", setup="s = set(range(10**6))", number=100000))
'''
