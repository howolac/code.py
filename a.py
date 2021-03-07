#！python3
#项目：生成随机的测验试卷文件
#.write()一次只能传入一个参数
#.keys()方法调用后换成list
#abcd很有灵性

import random, os

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'NewMexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'WestVirginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

#定义到桌面
os.chdir('c:\\users\\howolac\\desktop')

for i in range(35):
    keys = list(capitals.keys())
    #打开文件，写入基本信息，共35次
    file = open('capitalsquiz%s.txt' % (i + 1), 'w')
    fileanswer = open('answer%s' % (i + 1), 'w')

    file.write('Name:\nDaten:\nPeriod:\n' + ' ' * 20 +
               'State Capitals Quiz (Form %s)\n\n' % (i + 1))

    #打乱州的名称的顺序，一次写入1道问题，保存1个正确答案，
    # 加入三个错误答案，打乱4个答案，共50次

    for j in range(50):
        #因为values值等下要做删除，所以放到这里面
        values = list(capitals.values())
        correctanswer = []
        options = []
        random.shuffle(keys)

        file.write('%s.What is the capital of the %s:\n' % ((j + 1), keys[j]))
        fileanswer.write('%s.question=' % (j + 1))
        #加入正确答案，删除正确答案
        correctanswer = capitals[keys[j]]
        del values[values.index(correctanswer)]

        #加入打乱顺序的3个
        options = [correctanswer] + random.sample(values, 3)
        #把四个答案打乱顺序
        random.shuffle(options)
        #把正确答案写入answer文件中
        fileanswer.write('ABCD'[options.index(correctanswer)] + '\n\n')
        #依次打印出答案，并换行为下一题做好准备
        for k in range(4):
            file.write('ABCD'[k] + '.' + options[k] + '\n')
        file.write('\n')

file.close()
fileanswer.close()

#创建答案清单