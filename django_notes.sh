## start a django project - last one is the name 
django-admin startproject main

## to run django server 
python manage.py runserver

## create first django application 
python manage.py startapp restapi_yolo
## got to main/settings.py, add 'restapi_yolo' into installed app list


## in restapi_yolo/views.py add follow to create an index page
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello World!')
    
## make following changes in main/urls.py
from django.conf.urls import include
from restapi_yolo import views
urlpatterns = [
    url(r'^$',views.index,name ='index'),
    url(r'^restapi_yolo/',include('restapi_yolo.urls')),
    url(r'^admin/', admin.site.urls),
]


## create url.py in restapi_yolo folder 
from django.conf.urls import url
from restapi_yolo import views

urlpatterns =[
    url(r'^$',views.index,name='index')
]






