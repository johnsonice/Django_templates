from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

## giving some basic description for the default api view page
router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns=[
    #url(r'^hello-view/',views.HelloApiView.as_view()),
    url(r'',include(router.urls)) ## this one is telling it to look for urls in router
]
