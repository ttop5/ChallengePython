# 思路一：转换成同字符以后用in:

UPPER = a.upper()
if 'LOVE' in UPPER:
    print 'LOVE'
else:
    print 'SINGLE'

# 或者使用find

UPPER = a.upper()
if UPPER.find('LOVE') >= 0:
    print 'LOVE'
else:
    print 'SINGLE'


# 思路二：使用正则

import re

flag = re.findall("[lL][oO][vV][eE]",a)
if flag:
    print 'LOVE'
else:
    print 'SINGLE'
