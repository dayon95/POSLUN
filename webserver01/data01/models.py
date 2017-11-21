from django.db import models
from django.utils import timezone
#import django_filters

# Create your models here.

class PosterData(models.Model):
    title = models.CharField(max_length=10, default='default title')
    name = models.TextField(default='default name')
    when = models.TextField(default='default when')
    theme = models.TextField(default='default theme')
    goods = models.TextField(default='default goods')
    who = models.TextField(default='default who')
    where = models.TextField(default='default where')
    link = models.TextField(default='default link')
    how = models.TextField(default='default how')

    def __str__(self):
        return self.name

class pd1(models.Model): #하루행사
    title = models.CharField(max_length=20, default='default title')
    date = models.IntegerField(default='default date') #only date DateField
    starttime = models.IntegerField(default='default time') #only time TimeField
    endtime = models.IntegerField(default='default time')
    theme = models.TextField(default='default theme')
    who = models.CharField(max_length=20, default='default who')
    where = models.CharField(max_length=20, default='default where')

    def __str__(self):
        return self.title

class pd1_time(models.Model): #하루행사 시간
    title = models.CharField(max_length=20, default='default title')
    date = models.DateField(default='2000-01-01') #only date DateField
    starttime = models.TimeField(default='12:00') #only time TimeField
    endtime = models.TimeField(default='12:00')
    theme = models.TextField(default='default theme')
    who = models.CharField(max_length=20, default='default who')
    where = models.CharField(max_length=20, default='default where')

    def __str__(self):
        return self.title
