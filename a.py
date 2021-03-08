#！python3
#遍历目录树
#usage：压缩文件。注意先zip.namelist()之后才知道文件的名字，可能是a/a.txt
#但不是a.txt
#压缩文件夹似乎不会压缩文件夹里面的文件

import os, zipfile

os.chdir('c:\\users\\howolac\\desktop')

zip = zipfile.ZipFile('a.zip', 'w')
zip.write('sasa.txt', compress_type=zipfile.ZIP_DEFLATED)

zip.close()