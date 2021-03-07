#！python3
#遍历目录树
#usage：直接运行，浏览当前目录下所有且目录的目录所有且。。

import os

os.chdir('D:\\GAME')

#读取当前目录字符串，子文件夹name列表，其它文件name列表
for foderName, subfolders, fileNames in os.walk(os.getcwd()):
    #打印出：说明：当前目录
    print('current folder is : ' + foderName)
    #遍历打印出：当前目录的文件路径+‘：’+文件
    for subfolder in subfolders:
        print(foderName + 'sufolders :' + subfolder)
    for fileName in fileNames:
        print(foderName + 'file :' + fileName)
