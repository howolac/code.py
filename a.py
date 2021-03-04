#！python3
#正则表达式识别
#统计@名字模式的字符串出现次数
#用字典方法很巧妙地传入长字符串
#还有结尾有换行符号会导致打印出来看起来一样但结果却不一样，用.strip()
#没解决

import re


sum = [0] * 1000
k = 0

for i in range(len(a) - 1 - k):
    for j in a[i + 1:]:
        if a[i] == j:
            sum[i] += 1
            del a[i]
            i -= 1
            k += 1

for i in range(len(a) - k):
    a[i] = str(sum[i]) + ' ' + a[i]

print(sum,a)
