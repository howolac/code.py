#！python3
''' 
在每一行之前添加星号的小脚本

'''

import pyperclip


def add_star(a):
    a = a.split('\n')
    for i in range(len(a)):
        a[i] = '*' + a[i]
    a = '\n'.join(a)
    return a


a = pyperclip.paste()

a = add_star(a)

pyperclip.copy(a)

print(pyperclip.paste())