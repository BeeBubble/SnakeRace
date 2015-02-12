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
# print my_abs('a')


def nop():
    pass


print nop()

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print x, y

# 默认参数的坑
def add_end(L=[]):
    L.append('End')
    return L


print add_end()
print add_end()


def add_end2(L=None):
    if L is None:
        L = []
    L.append('End')
    return L


print add_end2()
print add_end2()

# 可变参数
def calc(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


print calc(1, 2, 3)

num1 = [1, 2, 3]
num2 = [4, 5, 6]
print calc(*num1)
print calc(*num2)


# 关键字参数
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)

# 参数组合


def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

args1 = (1, 2, 3, 4)
kw1 = {'d': 'b'}

func(*args1, **kw1)

# 递归函数


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print fact(1)
print fact(5)
print fact(10)
print fact(100)
# print fact(1000)

# 尾递归优化
import sys


class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is it's own grandparent, and catching such
    exceptions to fake the tail call optimization.

    This function fails if the decorated
    function recurses in a non-tail context.
    """

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back \
                and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException, e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def fact2(base, count):
    if count == 1:
        return base
    return fact2(base * (count - 1), count - 1)



print fact2(1000, 1000)
print fact2(100,100)
print fact2(100,10)


@tail_call_optimized
def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)


print fact_iter(1, 1, 1000)


# 返回函数
def lazy_sum(*args):
    def sum():
        sum = 0
        for arg in args:
            sum+=arg
        return sum
    return sum
f = lazy_sum(1,3,5,7,9)
print f
print f()
