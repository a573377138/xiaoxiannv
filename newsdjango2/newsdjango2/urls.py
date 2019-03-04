"""newsdjango2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include,re_path
from article.views import index,category,article,search,item,tag
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path(r'^$', index),
    path('category/', category, name='category'),
    path('article/', article, name='article'),
    path('search/', search, name='search'),
    path('item/', item, name='item'),
    path('tag/', tag, name='tag'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)