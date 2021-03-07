#！python3
#项目：打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达式的所有行。
#
#用法：txt文件名字中间有一个空格不行,path add your path

import os, re

path = 'C:\\?'


txt_file = os.listdir('.')
for i in range(len(txt_file)):
    if txt_file[i][-1] == 't' and txt_file[i][-2] == 'x' and txt_file[i][
            -3] == 't' and txt_file[i][-4] == '.':
        continue
    else:
        del txt_file[i]


regex = re.compile(r'字符串')

for i in range(len(txt_file)):
    file = open(os.path.join(path, txt_file[i]), encoding='utf8')
    a = file.readlines()

    for j in range(len(a)):
        try:
            regex.search(a[j]).group()
            print(a[j])
        except:
            continue

