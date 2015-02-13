# -*- coding: utf-8 -*
__author__ = 'shawn'

# 偏函数
print int('12345')
print int('0x0011', base=16)
print int('0x00101', base=16)
print int('00101', base=16)
print int('00101', base=2)

import functools

int2 = functools.partial(int, base=2)
print int2('00101')

max2 = functools.partial(max, 10)
print max2(2, 3)
print max2(11, 9)

