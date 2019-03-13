from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View
from django.views.decorators.http import require_POST,require_GET
from apps.news.models import NewsCategory
from utils import restful
from .forms import EditNewsCategoryForm
import os
from django.conf import settings
import qiniu



@staff_member_required(login_url='index')
def index(request):
    return  render(request,'cms/index.html')


class Writenews(View):
    def get(self,request):
        categories = NewsCategory.objects.all()
        content = {
            'categories': categories
        }
        return render(request,'cms/write_news.html',context=content)



@require_GET
def news_category(request):
    categories=NewsCategory.objects.all()
    content={
        'categories':categories
    }
    return render(request,'cms/news_category.html',context=content)


@require_POST
def add_news_category(request):
    name = request.POST.get('name')
    exists = NewsCategory.objects.filter(name=name).exists()
    if not exists:
        NewsCategory.objects.create(name=name)
        return restful.ok()
    else:
        return restful.params_error(message='该分类已经存在！')

@require_POST
def edit_news_category(request):
    form=EditNewsCategoryForm(request.POST)
    if form.is_valid():
        pk=form.cleaned_data.get('pk')
        name=form.cleaned_data.get('name')
        try:
            NewsCategory.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error(message='该新闻分类不存在！')
    else:
        return restful.params_error(message=form.get_errors())


@require_POST
def delete_news_category(request):
    pk=request.POST.get('pk')
    try:
        NewsCategory.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.params_error(message='该分类不存在！')

@require_POST
def upload_file(request):
    file=request.FILES.get('file')
    name=file.name
    with open(os.path.join(settings.MEDIA_ROOT,name),'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    url=request.build_absolute_uri(settings.MEDIA_URL+name)
    return restful.result(data={'url':url})

@require_POST
def qntoken(request):
    access_key='rH44NiA-I5aggh_VeEVC13rqcaJzxXOreqKuM-Qh'
    secret_key='8MZ7FHAbzC_9xVzvaHBXC2Ai6TByrGuShrSuPuoc'
    bucket='xiao_xiannv'
    q=qiniu.Auth(access_key,secret_key)

    token=q.upload_token(bucket)

    return restful.result(data={'token':token})
