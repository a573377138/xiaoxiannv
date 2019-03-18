#-*- coding: utf8 -*-
from utils import restful
from django.shortcuts import reverse,render,redirect

def xfz_login_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            if request.is_ajax():
                return restful.unauth(message='登录之后才能评论哟，请先登录！')
            else:
                return redirect('/')

    return wrapper