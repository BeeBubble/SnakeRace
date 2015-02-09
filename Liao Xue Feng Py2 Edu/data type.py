# -*- coding: utf-8 -*
__author__ = 'shawn'

# 内部不转义
print '\\\n\\'
print r'\\\n\\'

# 换行
print '''
this
is
my
python
world
'''

# boolean
print 3 > 2
print 2 < 3 and 5 < 4
print not True

# pointer
a = 'abc'
b = a
a = "xyz"
print 'a='+a, 'b='+b

# 除法
print 10/3
print 10.0/3

