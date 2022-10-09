from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Сourses, Category, Cart


class СoursesSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(
        choices=((True, "online"),
                 (False, "offline"))
    )
    class Meta:
        model = Сourses
        fields = ['id','user', 'category','company','name', 'type','image', 'description', 'price', 'created_date', 'website','job_openings', 'adress']

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
        fields = ['user', 'courses']


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['courses']
