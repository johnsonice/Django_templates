from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('Hello World!')
    my_dict = {'insert_me':'This is from views.py index function'}
    return render(request,'yolo/index.html',context=my_dict) #render functio knows to look for index.html in templates folder 

def image(request):
    my_dict = {'img_path':'images/preview.png'}
    return render(request,'yolo/image.html',context=my_dict) #render functio knows to look for index.html in templates folder 


