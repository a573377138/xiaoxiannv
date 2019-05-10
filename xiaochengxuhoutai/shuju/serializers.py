#-*- coding: utf8 -*-
from rest_framework import serializers
from .models import News,Category

class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']
class Newsserializers(serializers.ModelSerializer):
    category=Categoryserializers()
    class Meta:
        model=News
        fields=['id','category','title','thumbnail','time']

class NewsDetailsri(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['id','title','content','time']