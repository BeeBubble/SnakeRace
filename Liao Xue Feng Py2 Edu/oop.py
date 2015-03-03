# -*- coding: utf-8 -*
__author__ = 'shawn'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


shawn = Student('Shawn', 99)
shawn.print_score()

print shawn.get_grade()

print shawn.name
print shawn.score

# 私有成员变量

class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('invalid score')


jesielin = Student2('jesielin', 20)
jesielin.set_name('shawn')
jesielin.set_score(11)
print jesielin.get_name()
print jesielin.get_score()

# 多态
class Animal(object):
    def run(self):
        print 'animal is running'


class Dog(Animal):
    def run(self):
        print 'dog is running'


def run_twice(a):
    if isinstance(a, Animal):
        a.run()
        a.run()


run_twice(Animal())
run_twice(Dog())

# 类型 type()
print type(123)
dog = Dog()
print type(dog)
print type(Animal())
print type(Animal)
print type(abs)

import types

print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TypeType

# 判断一个变量是否是某些类型中的一种
print isinstance(dog, (str, unicode))

# 获得对象的所有属性和方法 dir()
print dir(dog)

# len()方法实际调用的是对象本身的__len__()方法
class L(object):
    def __len__(self):
        return 2


print len(L())

# hasattr setattr getattr
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print hasattr(obj, 'x')
print hasattr(obj, 'y')
setattr(obj, 'z', 3)
print getattr(obj, 'z')
fn = getattr(obj, 'power')
print fn()