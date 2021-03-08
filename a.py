#！python3
#遍历目录树
#usage：解压文件到桌面。注意先zip.namelist()之后才知道文件的名字，可能是a/a.txt
#但不是a.txt

import os, zipfile

os.chdir('c:\\users\\howolac\\desktop')

zip = zipfile.ZipFile('a.zip')


zip.extract('a/a.txt')
zip.close()