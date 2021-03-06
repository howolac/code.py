#！python3
#正则表达式
#匹配名字

import re, pyperclip

regex = re.compile(r'([A-Z][a-z]+\s[A-Z][a-z]+)')
print(
    regex.findall('''该正则表达式必须匹配：
 'Satoshi Nakamoto'
 'Alice Nakamoto'
 'RoboCop Nakamoto'
但不匹配：
 'satoshi Nakamoto'（名字没有大写首字母）
 'Mr. Nakamoto'（前面的单词包含非字母字符）
 'Nakamoto' （没有名字）
 'Satoshi nakamoto'（姓没有首字母大写）

'Mr. Nakamoto'
'''))
