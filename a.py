#！python3
#正则表达式识别
#统计@名字模式的字符串出现次数
#用字典方法很巧妙地传入长字符串
#还有结尾有换行符号会导致打印出来看起来一样但结果却不一样，用.strip()

import re

a = {'game':}

a = str(a.values())

b = a.strip()
sum = [0] * 1000

regex = re.compile(r'@\w+')
c = regex.findall(b)

for i in range(len(c) - 1):
    for j in c[i + 1:]:
        if c[i] == j :
            sum[i] += 1

for i in range(len(c)):
    c[i] = str(sum[i]) + ' ' + c[i]

print(c)
