#-*- coding: utf8 -*-
from django.urls import path
from . import views
app_name='shuju'

urlpatterns=[
    path('',views.index,name='index'),
    path('addnews/',views.addnews,name='addnews'),
    path('news_list/',views.newslist,name='news_list'),
    path('hotnews/',views.hotnews,name='hotnews'),
    path('news_detail/',views.news_detail,name='news_detail')
]