#！python3
#正则表达式
'''如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。否
则，函数第二个参数指定的字符将从该字符串中去除。
'''

import re, pyperclip


def sta(x, y=''):
    if y == '':
        regex = re.compile(r'(\s*)(((.)+)(\S))(\s*)', re.DOTALL)
        t = regex.search(x)

        print('clear it!')

        return t.group(2)
    else:
        t = []

        for i in range(len(x)):
            if x[i] != y:
                t += x[i]

        print('clear ', y)

        return ''.join(t)


pyperclip.copy(sta(pyperclip.paste()))
