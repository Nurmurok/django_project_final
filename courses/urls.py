from django.urls import path

from .views import (СoursesListApiView, GetCartAPIView,CoursesCreateAPIView,CategoryListApiView
)


urlpatterns = [
    path('list/', СoursesListApiView.as_view(), name='list'),
    path('cat_list/', CategoryListApiView.as_view(), name='list'),
    path('cart/<int:id>', GetCartAPIView.as_view(), name='cart'),
    path('create/', CoursesCreateAPIView.as_view(), name='create')
]