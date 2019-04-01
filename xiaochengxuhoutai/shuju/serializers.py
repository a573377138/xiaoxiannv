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
        fields='__all__'