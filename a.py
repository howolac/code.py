#！python3
#项目：批量将美国风格的日期替换成欧洲风格的日期
#usage：把有美国风格日期的有txt的文件夹的路径加入进去，替换成欧洲风格的日期
#不能移动给itself。。。→要指明文件！
#regext.search()返回None或着可以用try： except：

import os, re, shutil

os.chdir('c:\\users\\howolac\\desktop')

path = 'c:\\users\howolac\\desktop'
#用os.listdir()找到所有文件名
filenames = os.listdir(path)
#创建一个识别美国日期的正则表达式
regex = re.compile(
    r'''(^(.*?)
    ((0|1)?\d)-  #一个或两个月的数字
    ((0|1|2|3)?\d)-(  #一个或两个关于日的数字
    ((19|20)\d\d)   #四个关于年份的数字
    (.*)?       #非贪心匹配剩下的所有字符  
#这里可以试着替换成(.*?)   ，结果会是这个不匹配字符 (.*)?  like (.*),just have or not

))''', re.VERBOSE)
#保存下面筛选出来的文件d额list
kongnew = []
kongold = []
#遍历每一个文件来筛选出带有美国风格的日期
#bing修改美国风格的日期成欧洲风格的
for i in filenames:
    try:
        regex.search(i).group()
        print
        kongold += [i]
        #用括号调换一下中间位置和第一个位置
        #最好一个变量一个变量列出来而不是一次性写出来
        kongnew += [
            regex.search(i).group(2) + regex.search(i).group(5) + '-' +
            regex.search(i).group(3) + '-' + regex.search(i).group(7)
        ]
    except:
        continue

#用shutil.move()函数来移动文件
#for 从当前路径移动到当前路径
for i in range(len(kongnew)):
    print('Changing ' + kongold[i] + 'to ' + kongnew[i])
    shutil.move(kongold[i], kongnew[i])

print('done')
