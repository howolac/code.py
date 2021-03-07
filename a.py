#！python3
#项目：疯狂填词
#用法：根据程序提示，对一个语句中的一些词进行替换

a = '''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.'''

#分割字符串
a = a.split(' ')

#找到那些地方，提示用户输入以替换
for i in range(len(a)):
    if a[i] == 'ADJECTIVE' or a[i] == 'NOUN' or a[i] == 'ADVERB' or a[
            i] == 'VERB':
        print('Enter an ' + a[i].lower())
        a[i] = input()
print(' '.join(a))