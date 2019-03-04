from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def book(request):
    return HttpResponse('图书首页')
def book_detail(request,book_id,fenlei_id):
    text ='您获取的图书ID是：%s，图书分类：%s' % (book_id,fenlei_id)
    return HttpResponse(text)
def author_detail(request):
    author_id = request.GET.get('id')
    text ='作者的ID是：%s' %author_id
    return HttpResponse(text)
def xiaoxiannv(request,name):
    text = '你是谁？你是：%s吗？最漂亮的那个%s' % (name,name)
    return HttpResponse(text)