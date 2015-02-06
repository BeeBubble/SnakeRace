# -*- coding: utf-8 -*
__author__ = 'shawn'

help(abs)

print abs(100)

print cmp(1.1, 2.2)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad args.')
    if x >= 0:
        return x
    else:
        return -x


print my_abs(-100)
print my_abs(2.2)
print my_abs('a')


def nop():
    pass


print nop()
