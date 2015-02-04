# -*- coding: utf-8 -*
__author__ = 'shawn'

print ord('A')
print chr(65)
print unichr(65)

print u'世界'
print u'世界'.encode('utf-8')
print len(u'世界'.encode('utf-8'))
print len(u'世界')

# 格式化
print 'Hello,%s' % 'AAA'
print '%2d-%012d' % (3, 1)
print '%.2f' % 3.1415926
print '''Age:%s.Gender:%s
growth rate:%s%%''' % (25,True,90)