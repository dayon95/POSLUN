import xlrd
#from xlutils.copy import copy

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webserver01.settings")

import django
django.setup()

from data01.models import PosterData
from data01.models import pd1
from data01.models import pd1_time

wb = xlrd.open_workbook(os.path.join("C:\django_gegche\dproject01\POSLUN", "hakguan_db.xlsx"))
sheet = wb.sheet_by_index(0)
num_r = sheet.nrows

for i in range(1,num_r):
    row = PosterData(title = sheet.row_values(i)[0], name = sheet.row_values(i)[1], \
                   when = sheet.row_values(i)[2], theme = sheet.row_values(i)[3], \
                   goods = sheet.row_values(i)[4], who = sheet.row_values(i)[5], \
                   where = sheet.row_values(i)[6], link = sheet.row_values(i)[7], how = sheet.row_values(i)[8])
    row.save()

sheet2 = wb.sheet_by_index(1)
num_r2 = sheet2.nrows

for i in range(1,num_r2):
    row2 = pd1(title = sheet2.row_values(i)[0], date = sheet2.row_values(i)[1], \
                   starttime = sheet2.row_values(i)[2], endtime = sheet2.row_values(i)[3], \
                   theme = sheet2.row_values(i)[4], who = sheet2.row_values(i)[5], \
                   where = sheet2.row_values(i)[6], )
    row2.save()

"""
sheet3 = wb.sheet_by_index(2)
num_r3 = sheet3.nrows

for i in range(1,num_r3):
    row3 = pd1_time(title = sheet3.row_values(i)[0], date = sheet3.row_values(i)[1], \
                   endtime = sheet3.row_values(i)[2], theme = sheet3.row_values(i)[3], \
                   who = sheet3.row_values(i)[4], where = sheet3.row_values(i)[5], \
                   starttime = sheet3.row_values(i)[6], )
    row3.save()

"""
    
