#-*- coding: utf8 -*-
from django.urls import path
from . import views
app_name='vvuuee'
urlpatterns = [
    path('index',views.index,name='index'),
    path('upload/',views.upload,name='upload')
]
