from django.db import models

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
    
