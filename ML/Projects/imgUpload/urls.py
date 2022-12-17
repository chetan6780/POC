
from django.urls import path
from django.conf.urls import include,url
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    url(r'imageprocess', views.imageprocess,name='imageprocess'),
]
