#！python3
#项目：打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达式的所有行。
#
#用法：txt文件名字中间有一个空格的不行→可以！！！

import os, re

#改变当前路径
path = 'path'
os.chdir(path)

#遍历文件列表
a = os.listdir()
#创建一个找txt文件的正则表达式
regex = re.compile(r'字符串')

for i in range(len(a)):
    #判断是否log文件
    if a[i][-1] == 't' and a[i][-2] == 'x' and a[i][-3] == 't':
        #打开文件
        file = open(a[i], 'r', encoding='utf8')
        #便利每个文件的每一行
        b = file.readlines()

        for j in range(len(b)):
            #找出这所有有字符串的行，并打印出来
            try:
                regex.search(b[j]).group()
                print(b[j])
            except:
                continue
        file.close()
