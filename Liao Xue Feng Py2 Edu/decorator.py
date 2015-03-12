# -*- coding: utf-8 -*
__author__ = 'shawn'

# 装饰器
def now():
    print '2015-02-12'


now()


def log(f):
    def wrapper(*args, **kw):
        print '%s call %s():' % (__author__, f.__name__)
        return f(*args, **kw)

    return wrapper


@log
def now2():
    print '2015-02-12'


now2()

import functools


def log2(text):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print '%s %s call %s():' % (text, __author__, f.__name__)
            return f(*args, **kw)

        return wrapper

    return decorator


@log2('aaa')
def now3():
    print '2015-02-12'


now3()
print now2.__name__
print now3.__name__

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 再思考一下能否写出一个@log的decorator，使它既支持：
# @log
# def f():
# pass
#
# 又支持：
#
# @log('execute')
# def f():
# pass
def decorator(text='execute'):
    def d(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print 'begin call %s' % text
            f(*args, **kw)
            print 'end call'

        return wrapper

    return d


@decorator()
def now4():
    print '2015-02-15'


@decorator('bb')
def now5():
    print '2015-02-16'


now4()
now5()
