# -*- coding: utf-8 -*
__author__ = 'shawn'


def is_odd(n):
    return n % 2 == 1


print filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def not_empty(n):
    return n and n.strip()


print filter(not_empty, ['A', '', 'B', '', 'D'])

# 请尝试用filter()删除1~100的素数。
def is_prime(n):
    index = 2
    while index < n / 2 and n % index != 0:
        index += 1
    return index < n / 2


print filter(is_prime, range(1, 100))