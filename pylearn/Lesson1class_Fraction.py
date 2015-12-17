#################################################
import decimal

decimal.getcontext().prec = 5
a = decimal.Decimal(1) / decimal.Decimal(3)

print(a)
##################################################
from fractions import Fraction

b1 = Fraction(1, 3)
b2 = Fraction(5, 9)
b3 = b1 + b2

print(b3)
##################################################
c1 = 'Let\'s'
c2 = 'begin.'
c3 = '{b} try to {a}'.format(a = c2, b = c1)
print(c3)
##################################################