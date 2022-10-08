from django.urls import path

from .views import (СoursesListApiView, GetCartAPIView, CoursesCreateAPIView, CategoryListApiView,
                    CategoryCreateApiView, FilterByCategory,FilterByPrice
                    )


urlpatterns = [
    path('list/', СoursesListApiView.as_view(), name='list'),
    path('cat_list/', CategoryListApiView.as_view(), name='list'),
    path('cart/<int:id>', GetCartAPIView.as_view(), name='cart'),
    path('create/', CoursesCreateAPIView.as_view(), name='create'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat_create'),
    path('filterByCategory/<slug:name>/', FilterByCategory.as_view(), name='filter'),
    path('filterByPrice/<slug:name>/<int:price>', FilterByPrice.as_view(), name='filter_price'),


]