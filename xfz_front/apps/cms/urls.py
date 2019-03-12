from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('',views.index,name='index'),
    path('writenews/',views.Writenews.as_view(),name='writenews'),
    path('news_category/', views.news_category, name='news_category'),
]