"""mynews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import article.views
import django.views.static
urlpatterns = [
    url('admin/', admin.site.urls),
    url('$',article.views.index,name='index'),
    url('category/', article.views.category,name='category'),
    url('article/', article.views.article,name='article'),
    url('search/', article.views.search, name='search'),
    url('category/', article.views.category, name='category'),
    url('item/', article.views.item, name='item'),
    url('tag/', article.views.tag, name='tag'),
    url('ueditor/', include('DjangoUeditor.DjangoUeditor.urls')),
    url('media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

]
