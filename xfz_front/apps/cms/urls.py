from django.urls import path
from . import views
from . import course_views

app_name = 'cms'

urlpatterns = [
    path('',views.index,name='index'),
    path('write_news/',views.Writenews.as_view(),name='write_news'),
    path('edit_news/',views.EditNews.as_view(),name='edit_news'),
    path('delete_news/',views.delete_news,name='delete_news'),
    path('news_category/', views.news_category, name='news_category'),
    path('add_news_category/',views.add_news_category,name='add_news_category'),
    path('edit_news_category/',views.edit_news_category,name='edit_news_category'),
    path('banners/',views.banners,name='banners'),
    path('delete_news_category/',views.delete_news_category,name='delete_news_category'),
    path('banners/',views.banners,name='banners'),
    path('add_banner/',views.add_banner,name='add_banner'),
    path('banner_list/',views.banner_list,name='banner_list'),
    path('delete_banner/',views.delete_banner,name='delete_banner'),
    path('edit_banner/',views.edit_banner,name='edit_banner'),
    path('upload_file/',views.upload_file,name='upload_file'),
    path('qntoken/',views.qntoken,name='qntoken'),
    path('news_list/',views.NewsListView.as_view(),name='news_list')
]

urlpatterns += [
    path('pub_course/',course_views.PubCourse.as_view(),name='pub_course'),
    path('course_category/',course_views.course_category,name='course_category'),
    path('add_course_category/',course_views.add_course_category,name='add_course_category'),
    path('edit_course_category/',course_views.edit_course_category,name='edit_course_category'),
    path('delete_course_category/',course_views.delete_course_category,name='delete_course_category'),
    path('addcourse_teacher/',course_views.AddCourse_Teacher.as_view(),name='addcourse_teacher'),
    path('teacher_list/',course_views.course_teacher_list,name='teacher_list'),
    path('delete_teacher/',course_views.delete_teacher,name='delete_teacher')
]