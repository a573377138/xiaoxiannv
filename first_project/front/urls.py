#-*- coding: utf8 -*-
from django.urls import path
from . import views

app_name='front'
urlpatterns = [
    path('',views.index,name='index'),
    path('sigin/',views.login,name='login')
]