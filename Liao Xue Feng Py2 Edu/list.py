# -*- coding: utf-8 -*
__author__ = 'shawn'

classmates = ['Michael','Bob','Tracy']
print classmates

print 'len:',len(classmates)
print classmates[1]
print classmates[-1]

classmates.append('Shawn')
print classmates

classmates.insert(2,'AAA')
print classmates

print classmates.pop()
print classmates

print classmates.pop(2)
print classmates

classmates[2] = 'BBB'
print classmates

L = ['A','B','C']
classmates.append(L)
print classmates
print classmates[3][2]
print classmates[2][2]

