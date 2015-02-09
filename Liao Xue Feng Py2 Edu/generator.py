# -*- coding: utf-8 -*
__author__ = 'shawn'

g = (x * x for x in range(100))
print g
print g.next()
print g.next()
for key in g:
    print g.next()


def fib(max):
    n, a, b = 0, 0, 1
    x = 0
    while (x < max):
        print b
        a, b = b, a + b
        x = x + 1


fib(100)


def fib2(max):
    n, a, b = 0, 0, 1
    while (n < max):
        yield b
        a, b = b, a + b
        n = n + 1


print fib2(100)

# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5


for a in odd():
    print a
odd()