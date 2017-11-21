from django.shortcuts import render
from data01.models import PosterData
import datetime


# Create your views here.

def test(request):
    return render(request,'data01/test.html',{})

def test_title(request):
    Poster_list=PosterData.objects.exclude(title__exact='')
    return render(request,'data01/test_title.html',{'Poster_list':Poster_list})

#아래에 있는 함수는 PosterData의 when을 datafield로 변경된 후에 실행가능함.
'''def index(request):
    today=datetime.today()
    tomorrow=today+datetime.timedelta(days=1)
    this_week=today.isocalendar()[1] #week number

    today_list=PosterData.objects.filter(when__year=today.year, when__month=today.month, when__day=today.day)
    tomorrow_list=PosterData.objects.filter(when__year=tomorrow.year, when_month=tomorrow.month, when__day=tomorrow.day)
    this_week_list=PosterData.objects.filter(when__week=this_week)

    contents={'today_list':today_list,'tomorrow_list':tomorrow_list,'this_week_list'=this_week_list}
    return render(request,'index site',contents)

def about(request):
    return render(request,'about site')
'''
