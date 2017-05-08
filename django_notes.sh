## start a django project - last one is the name 
django-admin startproject main

## to run django server 
python manage.py runserver

## create first django application 
python manage.py startapp restapi_yolo
## got to main/settings.py, add 'restapi_yolo' into installed app list


## after create model run migrate 
python manage.py migrate 
python manage.py makemigrations yolo
python manage.py migrate     ## do it one more time 

## create super for admin 
python manage.py createsuperuser
	## user name : chengyu
	## password : JOHNSONice16
	## email: huangchengyu16@gmail.com

## now you can go to admin page 
## http://127.0.0.1:8000/admin