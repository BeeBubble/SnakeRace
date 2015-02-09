# -*- coding: utf-8 -*
__author__ = 'shawn'


def f(x):
    return x * x


print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def add(x, y):
    return x + y


print reduce(add, [1, 3, 5, 7, 9])

# 自己写一个int()


def ten(x, y):
    return 10 * x + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print reduce(ten, map(char2num, '13579'))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def gf(s):
    s = s[0].upper() + s[1:].lower()

    return s


print map(gf, ['AAA', 'adam', 'LISA', 'barT'])


def format_str(s):
    # return temp[0].upper()
    L = []
    index = 0
    while index < len(s):
        if index == 0:
            L.append(s[index].upper())
        else:
            L.append(s[index].lower())
        index += 1
    return ''.join(map(str, L))


print map(format_str, ['AAA', 'adam', 'LISA', 'barT'])
print 'a'.upper()
print format_str('aa')
print format_str('AA')


def p(x, y):
    return x * y


print reduce(p, [1, 2, 3, 4, 5])


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(s):
    if not isinstance(s, list):

        return "请输入一个list"

    else:

        return reduce(lambda x, y: x * y, s)


print prod([1, 2, 3, 4, 5])