from django.contrib import admin

# Register your models here.

from .models import PosterData
from .models import pd1
from .models import pd1_time

admin.site.register(PosterData)
admin.site.register(pd1)
admin.site.register(pd1_time)
