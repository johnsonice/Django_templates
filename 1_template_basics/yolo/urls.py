from django.conf.urls import url
from yolo import views

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^image',views.image,name='image'),
]
