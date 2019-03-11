from django.shortcuts import render,reverse,redirect
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_POST
from .forms import LonginForm
from django.http import JsonResponse
from utils import restful
from django.http import HttpResponse
from utils.captcha.xfzcaptcha import Captcha
from io import BytesIO
from utils import smssender
from django.core.cache import cache
from .models import User
from .forms import RegisterForm


@require_POST
def login_view(request):
    form = LonginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request,username= telephone,password=password)
        if user:

            if user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.ok()
            else:
                return restful.unauth(message='账号被冻结！')
        else:
            return restful.params_error(message="手机或者密码错误！")
    else:
        eroors =form.get_errors()
        return restful.params_error(message=eroors)


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


@require_POST
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = User.objects.create_user(telephone=telephone,username=username,passwoerd=password)
        login(request,user)
        return restful.ok()
    else:
        print(form.get_errors())
        return restful.params_error(message=form.get_errors())

def sms_captcha(request):
    telephone=request.GET.get('telephone')
    code = Captcha.gene_text()
    cache.set(telephone,code,5*60)
    result=smssender.sms_captcha_sender(telephone,code)

    if result:
        return restful.ok()
    else:
        return restful.params_error(message='验证码发送失败')


def img_captcha(request):
    text,image=Captcha.gene_code()
    out= BytesIO()
    image.save(out,'png')
    out.seek(0)

    response = HttpResponse(content_type='image/png')
    response.write(out.read())
    response['Content-length']=out.tell()
    cache.set(text.lower(),text.lower(),5*60)
    return response

def test_memc(request):
    cache.set('user','houxianzhi',5*60)
    result=cache.get('user')
    print(result)
    return HttpResponse('success')