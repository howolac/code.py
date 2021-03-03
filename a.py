#！python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTab(a, long):
    for i in range(len(a[0])):
        for j in range(len(a)):
            print(a[j][i].rjust(long), end='')
        print('\n')


printTab(tableData, 10)
