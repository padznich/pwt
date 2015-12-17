""""
s = 'spam'
print(id(s))
s += 's'
print(id(s))
"""

'''
s2 = chr(97)
s3 = ord('a')

print(s2)
print(s3)
'''

s = 'spam'.encode('utf-8')
print(s)

a = s.decode('utf-8')
print(a)

print(isinstance(s, basestring))