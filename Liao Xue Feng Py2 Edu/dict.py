# -*- coding: utf-8 -*
__author__ = 'shawn'

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']

d['Michael'] = 100
print d['Michael']

if 'Michael' in d:
    print d['Michael']

print d.pop('Tracy')
print d