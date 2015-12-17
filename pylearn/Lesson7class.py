# coding=utf-8

#
# task 1
#
'''
a = 290
b = 90
c = 45

if a > b:
    d = a
    e = b
else:
    d = b
    e = a
if c > e:
    out = d + c
else:
    out = a + b
print(out)
'''


#
# task 2
#
'''
cost = 32.13
l = [i * cost for i in range(1, 11)]
print('стоимость кiлаграмау: {}'.format(l))
'''


#
# task 3
#
'''
cost = 32.43
i = 1.2
while i <= 2:
    print('За {}кг отдай {} денег'.format(i, i * cost))
    i += 0.2
'''


#
# task 4
#
'''
l = [i for i in range(2, 120, 2)]
for n in l:
    if len(str(n)) < 3:
        if n == 42:
            print('The Answer to the Ultimate Question of Life, the Universe, and Everything.')
            break
        print(n)
'''


#
# task 5
#
'''
l = [i for i in range(100)]
for i in l:
    if i % 13 != 0:
        continue
    else:
        print(i)
'''


#
# task 6
#
'''
import sys
l = sys.argv[1:]

s = 0
for i in l:
    s += int(i)
print(s)
'''


#
# task 7
#
'''
def candies(amount, cost):
    return(int(round(amount * cost, 0)))
print(candies(3.4, 5.84))
'''


#
# task 8
#
'''
def sum_args(*args):
    sum = 0
    for i in args:
        sum += i
    return(sum)
print(sum_args(1, 2, 3, 4, 5))
'''


#
# task 9
#
'''
def odd_even(*numbers):
    for i in numbers:
        if i % 2 == 0:
            print('An even number: {}'.format(i))
        else:
            print('An odd number: {}'.format(i))
    return False
odd_even(1, 2, 3, 4, 5, 6)
'''


#
# task 10
#
'''
def string_list(words):
    out = words.split()
    return out
print(string_list('er rt ty'))
'''



#
# task 11
#
'''
import sys
from datetime import date

us_input = (sys.argv[1]).split()
date1= (us_input[0]).split('-')
date2= (us_input[1]).split('-')
year1 = int(date1[0])
month1 = int(date1[1])
day1 = int(date1[2])
year2 = int(date2[0])
month2 = int(date2[1])
day2 = int(date2[2])

date1 = date(year1, month1, day1)
date2 = date(year2, month2, day2)

delta = date2 - date1
print(delta)
'''



#
# task 12
#
'''
def say(num):
    dict1 = {1: 'one', 2: 'two'}
    num = str(num)
    s = ''
    for w in num:
        s += '{} '.format(dict1[int(w)])
    return s.strip()
print(say(2112))
'''



#
# task 13
#
'''
t = {1, 2, 3, 4}
def odd_t(t):
    l1 = list(t)
    l2 = []
    for w in l1:
        if w % 2 == 0:
            l2.append(w)
    t2 = tuple(l2)
    return t2
print(odd_t(t))
'''


#
# task 14
#
'''
import argparse
from re import match

parser = argparse.ArgumentParser()
parser.add_argument('--filepath', type=str, required=True, help='Enter path to file.')
parser.add_argument('--pattern', type=str, required=True, help='Enter pattern.')
args = parser.parse_args()

filepath = args.filepath
pattern = '.*{}'.format(args.pattern)

with open(filepath, 'r') as file:
    lines_list = file.readlines()
for line in lines_list:
    if match(pattern, line):
        print(line)
'''



#
# task 15
#









#
# task 16
#
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, required=True, help='Enter path to file.')
parser.add_argument('--set_mode', type=str, default='union', help='Enter path to set mode.')
args = parser.parse_args()

file = args.file
set_mode = args.set_mode

with open(file, 'r') as file:
    slist = file.readlines()
s1 = set((slist[0]).split())
s2 = set((slist[1]).split())
out = 's1.{}(s2)'.format(set_mode)
out = eval(out)

# if set_mode == 'intersection':
#     out = s1.intersection(s2)
# elif set_mode == 'difference':
#     out = s1.difference(s2)
# elif set_mode == 'union':
#     out = s1.union(s2)
# else:
#     out = 'Wrong set_mode!'
print(out)
'''



#
# task 17
#
'''
import sys

try:
    num10 = int(sys.argv[1])
    print('num10 >> {}'.format(num10))
    print('num2 >> {}'.format(bin(num10)))
    print('num8 >> {}'.format(oct(num10)))
    print('num16 >> {}'.format(hex(num10)))
except Exception as e:
    print(e)
'''


#
# task 18
#
'''
import sys

def check_number():
    a = sys.argv[1]

    if int(a) < 0:
        print(type(a))
        raise Exception('The input value is integer, but less than zero.')
    else:
        return 'Input value is integer and above zero.'
print(check_number())
'''


#
# task 19
#
'''
import sys

a = sys.argv
def fin(a):
    try:
        a = float(sys.argv[1])
        b = 4 / a
    except ZeroDivisionError:
        return (ZeroDivisionError)
    except TypeError:
        return (TypeError)
    except ValueError:
        return (ValueError)
    finally:
        print("It's finally")
print(fin(a))
'''