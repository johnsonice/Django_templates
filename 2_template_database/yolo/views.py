from django.shortcuts import render
from django.http import HttpResponse
from yolo.models import Topic,Webpage,AccessRecord
import yolo.forms as forms

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

def uploadimage(request):
    if request.method == "POST":
        form = forms.uploadimage(request.POST,request.FILES)
        if form.is_valid():
            #do something here 
            print("Validation Success")
            handle_uploaded_file(request.FILES['image'])
            #print('Name:',form.cleaned_data['name'])
            #print('Email:',form.cleaned_data['email'])
            #print('Email:',form.cleaned_data['text'])
            return render(request,'yolo/showimage.html',{'form':form})
    else:
        form = forms.uploadimage()    
    return render(request,'yolo/imageupload.html',{'form':form}) 

def handle_uploaded_file(f):
    with open('static/images/in/test.jpg','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)