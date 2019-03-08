#-*- coding: utf8 -*-
from django import forms
from apps.forms import FormMixin

class LonginForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11,error_messages={'max_length':'手机号长度大于11位！'})
    password = forms.CharField(max_length=15,min_length=6, error_messages={"min_length":"密码最少不能少于6个字符","max_length":"密码最多不能超过15个字符"})
    remember = forms.IntegerField(required=False)

