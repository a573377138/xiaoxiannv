#-*- coding: utf8 -*-
from django import forms
from apps.forms import FormMixin

class EditNewsCategoryForm(forms.Form,FormMixin):
    pk=forms.IntegerField(error_messages={'required':'必须传入分类ID！'})
    name=forms.CharField(max_length=100)