#!python

#项目：消除缺失的编号
#描述：
'''在一个文件夹中，找到所有带指定前缀的文件，诸如 spam001.txt,
spam002.txt 等，并定位缺失的编号（例如存在 spam001.txt 和 spam003.txt，但不存
在 spam002.txt）。让该程序对所有后面的文件改名，消除缺失的编号。
'''
#usage：输入指定文件夹

import os, re, shutil

#path
path = 'c:\\users\\howolac\\desktop'

#设一个筛选所有该类型文件的正则表达式
#前缀设为'spam'
regext = re.compile(r'^(spam)\d{3}(.txt)$')
#筛选出所有该类型文件并加入列表
kong = []
for i in os.listdir(path):
    if regext.search(i) != None:
        kong += [i]

# 对列表进行排序
kong.sort()

number = 1
file_name = []
#先获得所有（len(kong)）标准名字
while (number - 1) < len(kong):
    if number < 10:
        file_name += ['spam' + '00' + str(number) + '.txt']
    elif number < 100:
        file_name += ['spam' + '0' + str(number) + '.txt']
    else:
        file_name += ['spam' + str(number) + '.txt']
    number += 1

#以列表长度遍历，如果不存在重命名
for i in range(len(kong)):
    if file_name != kong[i]:
        for i in range(len(kong[i:])):
            shutil.move(os.path.join(path, kong[i]),
                        os.path.join(path, file_name[i]))
    else:
        continue
