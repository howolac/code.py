#！python3
#正则表达式识别

import re

phonenum = re.compile(r'\d{3}-\d{3}-\d{3}')
a = 'My number is 415-555-4242.'
mo = phonenum.search(a)
print('phone number found ' + mo.group())
