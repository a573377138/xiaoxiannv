# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.contrib.auth.models import User
from DjangoUeditor.DjangoUeditor.models import UEditorField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20,verbose_name='名称')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = '新闻类别'
        verbose_name_plural = verbose_name
class Item(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')
    created_date = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    completed = models.BooleanField(default=False, verbose_name='是否完成')
    article_category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = '新闻子栏目'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    name=models.CharField(max_length=50,verbose_name=u'名称')
    slug=models.SlugField(max_length=50,verbose_name=u'描述')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    slug = models.SlugField(unique_for_year='publish_date', verbose_name='描述')
    author = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)
    # content = models.TextField(verbose_name='内容')
    content = UEditorField(u'内容', height=400, width=600, default='', imagePath="upload/",
                           toolbars='mini', filePath='upload/', blank=True)
    status = models.CharField(max_length=2, verbose_name='状态')
    tags = models.ManyToManyField(Tag, blank=True)
    publish_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='发布日期')
    expiration_date = models.DateTimeField(blank=True, null=True, verbose_name='有效日期')
    is_active = models.BooleanField(default=True, blank=True, verbose_name='是否热门')
    item = models.ForeignKey(Item, verbose_name='类别名称',on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='uploads', verbose_name='图片')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '新闻文章'
        verbose_name_plural = verbose_name

class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    pic = models.ImageField(upload_to='uploads', verbose_name='广告图')
    adurl = models.URLField(verbose_name='地址')
    adlocation = models.CharField(max_length=2, verbose_name='位置')  # a1,a2,a3,b1,b2,b3....
    status = models.CharField(max_length=1, default=1, verbose_name='状态')
