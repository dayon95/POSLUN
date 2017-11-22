from django.shortcuts import render
from data01.models import PosterData
from data01.models import pd1
from data01.models import pd1_time
from datetime import datetime, timedelta

# Create your views here.

def test(request):
    return render(request,'data01/test.html',{})

def test_title(request):
    Poster_list=PosterData.objects.exclude(title__exact='')
    return render(request,'data01/test_title.html',{'Poster_list':Poster_list})

def test_pd1(request):
    oneday=pd1.objects.exclude(title__exact='')
    return render(request,'data01/test_pd1.html',{'oneday':oneday})

def test_pd1_time(request):
    time=pd1_time.objects.exclude(title__exact='')
    return render(request,'data01/test_pd1_time.html',{'time':time})


#아래에 있는 함수는 PosterData의 when을 datafield로 변경된 후에 실행가능함.
def index(request):
    #today, tomorrow, this_week에는 오늘, 내일, 이번주의 주 번호가 들어감
    #주 번호는 52주 중 몇번째 주인지 나타내는 번호임
    #이 세개 변수는 python의 datetime 모듈을 사용했음.
    today=datetime.today()
    tomorrow=today+timedelta(days=1)
    this_week=today.isocalendar()[1] #week number
    date_KOR=["월", "화", "수", "목", "금", "토", "일"]
    date=date_KOR[today.weekday()]
    #today_list, tomorrow_list, this_week_list에는 각각 오늘 내일 이번주 강연 데이터가 들어있음
    #각각 조건에 맞는 filter를 이용하였음.
    today_list=pd1_time.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)
    tomorrow_list=pd1_time.objects.filter(date__year=tomorrow.year, date__month=tomorrow.month, date__day=tomorrow.day)
    this_week_list=pd1_time.objects.filter(date__week=this_week)
    #return render(request,'data01/index.html',today_list)
    contents={'date':date, 'today_list':today_list,'tomorrow_list':tomorrow_list,'this_week_list':this_week_list}
    return render(request,'data01/index.html',contents)
'''
def about(request):
    return render(request,'about site')
'''
