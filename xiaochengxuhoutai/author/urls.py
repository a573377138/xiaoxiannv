#-*- coding: utf8 -*-
from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
app_name='author'

urlpatterns=[
    path('login/',views.my_longin,name='login'),
    path('codeapi/',views.codeApi,name='codeapi'),
    path('longinC/',views.UserLogin.as_view(),name='longinC'),
    path('yanzheng/',obtain_jwt_token),
    path('chaxun/',views.chaxun,name='chaxun')
]
