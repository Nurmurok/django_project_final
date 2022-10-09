from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from courses.models import Cart
from .models import Account


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        write_only=True,
        required=True
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )
    is_vendor = serializers.ChoiceField(
        choices=((True, "vendor"),
                 (False, "user"))
    )




    class Meta:
        model = Account
        fields = ['email', 'username', 'is_vendor', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn`t match."}
            )
        return attrs


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields = ['user', 'courses']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']