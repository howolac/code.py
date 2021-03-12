#!python

import os, openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

os.chdir('c:\\users\\howolac\\desktop')

wb = openpyxl.load_workbook('1.xlsx')
sheet1 = wb.get_sheet_by_name('Sheet1')

#tuple(sheet['A1':'C3'])
#遍历所有行
for j in sheet1['A1':'C7']:
    for i in j:
        print(i.coordinate, i.value)
    print('---------------------------end of row---------------------------')
