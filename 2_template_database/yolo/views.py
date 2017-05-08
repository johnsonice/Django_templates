from django.shortcuts import render
from django.http import HttpResponse
from yolo.models import Topic,Webpage,AccessRecord
## Create your views here.
def index(request):
    #return HttpResponse('Hello World!')
    my_dict = {'insert_me':'This is from views.py index function'}
    return render(request,'yolo/index.html',context=my_dict) #render functio knows to look for index.html in templates folder 

def image(request):
    my_dict = {'img_path':'images/preview.png'}
    return render(request,'yolo/image.html',context=my_dict) #render functio knows to look for index.html in templates folder 


def accessrecord(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpages_list}
    return render(request,'yolo/accessrecord.html',context=date_dict) 