import xlrd
#from xlutils.copy import copy

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webserver01.settings")

import django
django.setup()

from data01.models import PosterData

wb = xlrd.open_workbook(os.path.join("C:\django_gegche\dproject01", "hakguan_db.xlsx"))
sheet = wb.sheet_by_index(0)
num_r = sheet.nrows

for i in range(1,num_r-1):
    row = PosterData(title = sheet.row_values(i)[0], name = sheet.row_values(i)[1], \
                   when = sheet.row_values(i)[2], theme = sheet.row_values(i)[3], \
                   goods = sheet.row_values(i)[4], who = sheet.row_values(i)[5], \
                   where = sheet.row_values(i)[6], link = sheet.row_values(i)[7], how = sheet.row_values(i)[8])
    row.save()
