from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test_title',views.test_title),
    url(r'^test',views.test),
]
