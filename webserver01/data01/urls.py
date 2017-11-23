from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test_pd1_time',views.test_pd1_time),
    url(r'^test_pd1_time',views.test_pd2),

    url(r'^test',views.test),
    url(r'^index',views.index),
    url(r'^index_tutorial',views.index_tutorial),
#    url(r'^about',views.about),
]
