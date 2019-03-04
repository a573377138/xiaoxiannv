"""shuju URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from qinduan import views as qin_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',qin_views.index,name='index'),
    path('diaoyu/',qin_views.diaoyu,name='diaoyu'),
    path('huizong/',qin_views.huizong,name='huizong'),
    path('renwu/',qin_views.renwu,name='renwu'),
    path('fuben/',qin_views.fuben,name='fuben'),
    path('denglu/',qin_views.dengluxx.as_view(),name='denglu'),
    path('renwu/renwuxq/',qin_views.renwuxq,name='renwuxq'),
    path('renwudaochu/',qin_views.quanliang,name='renwudaochu'),
    path('fuben/fubenxq/', qin_views.fubenxq, name='fubenxq'),
    path('fubendaochu/', qin_views.f_quanliang, name='fubendaochu'),
    path('diaoyudaochu/',qin_views.d_daochu,name='diaoyudaochu'),
    path('huizongdaochu/',qin_views.h_daochu,name='hzdaochu'),
    path('huizong/huizongxq/',qin_views.huizongxq,name='huizongxq'),
    path('diaoyu/diaoyuxq/',qin_views.diaoyuxq,name='diaoyuxq'),
    path('dangrirw/',qin_views.dangrirw,name='dangrirw'),
    path('dangrirw/drrenwuxq/',qin_views.drrenwuxq,name='drrenwuxq'),
    path('drrenwudaochu/',qin_views.r_quanliang,name='drdaochu')
]
