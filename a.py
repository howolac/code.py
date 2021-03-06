#！python3
#正则表达式
#强口令检测

import re

a = '1236aZa789'

try:
    re.compile(r'[a-z]').search(a).group()
    re.compile(r'[A-Z]').search(a).group()
    re.compile(r'[0-9]').search(a).group()
    print('强字符串')
except:
    print('not')
