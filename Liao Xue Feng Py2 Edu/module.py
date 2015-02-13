#!/usr/bin/env python
# -*- coding: utf-8 -*

' a test module '

__author__ = 'shawn'

# 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
#
# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
#
# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
#
# 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。
# 后面开始就是真正的代码部分。
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello world!'
    elif len(args) == 2:
        print 'Hello,%s!' % args[1]
    else:
        print 'Too many arguments!'


try:
    import json
except ImportError:
    import simplejson as json


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


import Image

im = Image.open('vic.jpg')
print im.format, im.size, im.mode
# print im.thumbnail((200,100))
# im.save('thumb.jpg','png')

import sys

print sys.path

if __name__ == '__main__':
    # print json.__author__
    # print json.__all__
    # print json.__doc__
    print greeting('awn')

    test()


