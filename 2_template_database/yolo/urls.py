from django.conf.urls import url
from yolo import views

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^uploadimage',views.uploadimage,name='imageupload'),
    url(r'^image',views.image,name='image'),
    url(r'^accessrecord',views.accessrecord,name='record'),
]
