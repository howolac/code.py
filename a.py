#！python3
#去掉字符串每行末尾的\n换行符

import pyperclip, re

t = pyperclip.paste()
regex = re.compile(r'[\n]')
regex = regex.sub('', t)

print(t)
