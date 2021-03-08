#!python

#项目：计算所有大于10gb的文件夹
#usage：向path传入目录就行了
#传入'c:\\users\\用户'会出现类似：
#\Application Data\\Application Data\\Application Data 找不到的错误

import os

#path
path = 'D:\\'

#遍历目录树，先找单独大文件的，再找大文件夹的

for folder, sub_folders, file_names in os.walk(path):
    #重置
    kong = 0
    for i in file_names:
        kong += os.path.getsize(os.path.join(folder, i))
    if kong > 10000000000:
        print(os.path.basename(folder) + str(kong))
