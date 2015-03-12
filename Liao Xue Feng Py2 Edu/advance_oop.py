# -*- coding: utf-8 -*
__author__ = 'shawn'

# 动态绑定Method
class Teacher(object):
    pass


def set_age(self, age):
    self.age = age


t = Teacher()

from types import MethodType

t.set_age = MethodType(set_age, t, Teacher)
t.set_age(25)
print t.age


# __slots__
class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'shawn'
s.age = 25

# slots 指定了只能动态绑定 name 和 age 两个属性
# s.score = 100


# @property 使用
class Student1(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


j = Student1()
j.score = 100
print j.score

# 多继承
class Mammal(object):
    pass


class RunnableMixin(object):
    pass


class CarnivorousMixin(object):
    pass


class Dog(Mammal, RunnableMixin, CarnivorousMixin):
    pass


print Dog
print dir(Dog)

# __str__
class Student2(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'student object (name:%s)' % self._name


print Student2('shawn')

# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器 a,b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print n


# __getitem__
class Fib2(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器 a,b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b

            return L


print Fib2()[3]
print Fib2()[5]
print Fib2()[3:9]

# __getattr__
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


print Chain().status.user.timeline.list

# __call__

class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


print Student3('shawn')()

ss = Student3('a')
print ss()

print callable(s)
print callable(ss)

# 动态构建类
def fn(self, name='world'):
    print 'hello , %s.' % name


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello('shawn')

# metaclass 编写ORM库 待完成