# -*- coding: utf-8 -*
__author__ = 'shawn'

# 切片
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print L
print L[0:2]
print L[2:4]
print L[:5]
print L[-2:]
print L[-3]
print L[-5:-1]

L = range(100)
print L

print L[:10:2]
print L[:]
print L[::10]

t = (0, 1, 2, 3, 4, 5)
print t[:4:2]

print 'Hello,world!'[-6:]

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key

for key in 'ABCD':
    print key

from collections import Iterable

print isinstance('ABCD', Iterable)
print isinstance(123, Iterable)  # 整数是否可迭代

for key, value in enumerate(t):
    print key, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

# 列表生成式
print [x * x for x in range(100)]
print [m + n for m in range(100) for n in range(50)]

import os

print [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录

A = range(1, 9)
A = [str(key) for key in A]
print [x + '*' + y for x in A for y in A if x == '1']

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in d.iteritems()]

L = ['Hello', 'World', 18, 'Apple', None]
print [key for key in L if isinstance(key,str)]
