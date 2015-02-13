# -*- coding: utf-8 -*
from __future__ import unicode_literals
from __future__ import division  # 引用这些可以在2.7环境下运行3.x的语法

__author__ = 'shawn'

# still run on Python 2.7
print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3