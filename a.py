#！python3
#项目：保存剪切板的内容并提供查询
#用法：三种输入模式：a.py save （想要的变量名）和a.py （要读取的变量名）
#和a.py list 所有存入的变量
#读取list的时候出现问题！！！----lower后面加()！！
#先list再str-----pyperclip.copy(str(list(data.keys())))
import pyperclip, shelve, os, sys

#切换到桌面
os.chdir('c:\\users\\howolac\\desktop')

data = shelve.open('data')

#根据输入参数判断用户想进行的操作，第一种，两参数，后一个为变量名
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    data[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    #如果是list就list
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(data.keys())))

    #如果是关键字就关键字
    elif sys.argv[1] in data.keys():
        pyperclip.copy(str(data[sys.argv[1]]))

data.close()