#!python

#项目：遍历一个目录树，查找特定扩展的文件（.txt），将它们拷贝到一个新的文件夹

#usage：向path传入目录就行了

import os, shutil

path_source = 'D:\\Program Files'
path_direction = 'C:\\users\\howolac\\desktop'

#判断是不是

for folder, sub_folders, file_names in os.walk(path_source):
    #判断文件是不是.dat结尾的,并把他们拷贝到桌面
    for i in file_names:
        if i.endswith('.dat'):
            shutil.copy(os.path.join(os.path.abspath(folder), i), path_direction)
            print('find ' + i)
