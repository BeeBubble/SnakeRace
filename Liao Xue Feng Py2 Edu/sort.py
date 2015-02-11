# -*- coding: utf-8 -*
__author__ = 'shawn'

print sorted([55, 79, 89, 74, 7468, 64, 4])


def reverse_cmp(x, y):
    if x < y:
        return 1
    if x > y:
        return -1
    return 0


print sorted([55, 79, 89, 74, 7468, 64, 4], reverse_cmp)


def cmp_ignore_case(s1,s2):
    s1 = s1.upper()
    s2 = s2.upper()
    if s1<s2:
        return -1
    if s1>s2:
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)