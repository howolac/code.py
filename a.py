#！python3
#正则表达式

import re, pyperclip

regex = re.compile(r'((\d{1,3})(,\d{3})*)')
print(regex.findall('''
'42'
'1,234'
'6,368,745'
'''))

'42'
'1,234'
'6,368,745'