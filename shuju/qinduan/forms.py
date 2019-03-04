#-*- coding: utf8 -*-

from django import forms
import django.utils.timezone as timezone
class mesesagecanshu(forms.Form):
    UU = forms.CharField(label='UUID')
    kssj = forms.CharField(min_length=5,max_length=20,label='开始时间')
    jssj = forms.CharField(min_length=5,max_length=20,label='结束时间')


class renwubiaodan(forms.Form):
    kssj = forms.DateTimeField(label='开始时间')
    jssj = forms.DateTimeField(label='结束时间')
    szsj = forms.DateTimeField(label='上周末时间')
    # kssj = forms.CharField(min_length=5,max_length=20,label='开始时间')
    # jssj = forms.CharField(min_length=5,max_length=20,label='结束时间')
    # szsj= forms.CharField(min_length=5,max_length=20,label='上周时间')