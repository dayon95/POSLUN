from django.shortcuts import render
from data01.models import pd1_time
from data01.models import pd2


# Create your views here.

def test(request):
    return render(request,'data01/test.html',{})

def test_pd1_time(request):
    time=pd1_time.objects.exclude(title__exact='')
    return render(request,'data01/test_pd1_time.html',{'time':time})

def test_pd2(request):
    time=pd2.objects.exclude(title__exact='')
    return render(request,'data01/test_pd2.html',{'two':two})
