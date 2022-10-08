from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import permissions
from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import filters, generics
from courses.models import Cart, Category, Сourses
from courses.serializers import СoursesSerializer
from .models import Account
from .permissions import AnonPermissionOnly
from .serializers import RegisterSerializer, UpdateSerializer, MyTokenObtainPairSerializer, UserSerializer


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # parser_classes = [JSONParser]
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                username=request.data['username'],
                email=request.data['email'],
            )
            user.set_password(request.data['password'])
            user.save()
            account = Account.objects.create(
                user=user,
                is_vendor=request.data['is_vendor']

            )
            account.save()
            cart = Cart.objects.create(
                user=user
            )
            cart.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        accounts = Account.objects.all()
        serializer = UserSerializer(accounts, many=True)
        return Response(serializer.data)


class UserDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)
        posts = Сourses.objects.filter(author_id=id)
        serializer = UserSerializer(user)
        serializer2 = СoursesSerializer(posts, many=True)
        data = serializer.data
        data['courses'] = serializer2.data
        data['quantity_of_courses'] = posts.count()
        return Response(data)


class UserDestroyApiView(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

