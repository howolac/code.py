#！python3
#读写本地文件

import os

os.chdir('c:\\users\\name\\desktop')

baconFile = open('bacon.txt', 'w')
print(baconFile.write('Hellso,File\n'))
baconFile.close()

baconFile = open('bacon.txt', 'a')
print(baconFile.write('Helslo,Fdile\n'))
baconFile.close()