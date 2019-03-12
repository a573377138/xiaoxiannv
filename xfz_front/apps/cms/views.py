from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View

@staff_member_required(login_url='index')
def index(request):
    return  render(request,'cms/index.html')


class Writenews(View):
    def get(self,request):
        return render(request,'cms/write_news.html')




def news_category(request):
    return render(request,'cms/news_category.html')