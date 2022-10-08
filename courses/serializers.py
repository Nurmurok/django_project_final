from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Сourses, Category, Cart


class СoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сourses
        fields = ['id','user', 'category', 'name','description', 'price', 'created_date', 'website', 'adress', 'latitude', 'longitude']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'user', 'courses']


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['courses']
