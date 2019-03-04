#-*- coding: utf8 -*-
from django import template
register = template.Library()
@register.filter
def jiadian(book,arg):
    return book+'.'+int(arg)