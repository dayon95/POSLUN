from django.shortcuts import render
from data01.models import PosterData

# Create your views here.

def test(request):
    return render(request,'data01/test.html',{})

def test_title(request):
    Poster_list=PosterData.objects.exclude(title__exact='')
    return render(request,'data01/test_title.html',{'Poster_list':Poster_list})
