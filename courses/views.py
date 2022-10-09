from django.db.models import Q
from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import filters, generics
from account.permissions import IsVendor
from .models import Сourses, Cart, Category
from rest_framework.views import APIView
from .serializers import СoursesSerializer, CartSerializer, UpdateSerializer, CategorySerializer
from rest_framework import permissions, status
from django.core.paginator import Paginator
from django_filters.rest_framework import DjangoFilterBackend


class СoursesListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    # def get(self,request):
    #     products=Сourses.objects.all()
    #     serializer = СoursesSerializer(products, many=True)
    #     return Response(serializer.data)


    def get(self,  request):
        courses = Сourses.objects.all()
        count = courses.count()
        paginator = Paginator(courses, 6)
        page_num = self.request.query_params.get('page', 1)

        serializers = СoursesSerializer(paginator.page(page_num), many=True)
        return Response({
            "count": count,
            "courses": serializers.data
        })


class CategoryListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,request):
        category=Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class CoursesCreateAPIView(APIView):
    # permission_classes = [IsVendor]
    permission_classes = [permissions.AllowAny]
    serializer_class=СoursesSerializer
    def post(self, request):
        serializers = СoursesSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCartAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]
    def get(self,request,id):
        cart = Cart.objects.get(user_id=id)
        courses = cart.courses.all()
        serializer2 = СoursesSerializer(courses, many=True)
        serializer = CartSerializer(cart)
        data = serializer.data
        data['courses'] = serializer2.data
        return Response(data)

    def put(self, requests,id):
        cart = self.get_object(id)
        serializer = UpdateSerializer(cart, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CategoryCreateApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class FilterByCategory(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, name):
        category = self.get_object(name)
        courses = Сourses.objects.filter(category__name=name)
        serializer = CategorySerializer(category)
        serializer2 = СoursesSerializer(courses, many=True)
        data = serializer.data
        data['courses'] = serializer2.data

        return Response(data)


class FilterCategoryByPrice(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, name, price):
        category = self.get_object(name)
        courses = Сourses.objects.filter(Q(category__name=name) & Q(price__gte=int(price)))
        serializer = CategorySerializer(category)
        serializer2 = СoursesSerializer(courses, many=True)
        data = serializer.data
        data['courses'] = serializer2.data

        return Response(data)


class FilterPrice(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get(self, request, price):

        courses = Сourses.objects.filter(price__gte=int(price))
        serializer2 = СoursesSerializer(courses, many=True)
        data = serializer2.data
        # data['courses'] = serializer2.data

        return Response(data)


class CreateCourseAPIView(APIView):
    def post(self, request):
        if request.data.get('course'):
            Cart.objects.get(user=request.user).courses.add(
                Сourses.objects.get(pk=request.data["course"])
            )
            return Response("Success", status=status.HTTP_200_OK)
        return Response("Error", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        if request.data.get('course'):
            cart = Cart.objects.get(user=request.user)
            course = Сourses.objects.get(pk=request.data["course"])
            if course in cart.courses.all():
                cart.courses.remove(
                        course
                    )

            return Response("Success", status=status.HTTP_200_OK)
        return Response("Error", status=status.HTTP_404_NOT_FOUND)