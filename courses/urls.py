from django.urls import path

from .views import (–°oursesListApiView, GetCartAPIView, CoursesCreateAPIView, CategoryListApiView,
                    CategoryCreateApiView, FilterByCategory,FilterCategoryByPrice,FilterPrice,
                    CreateCourseAPIView
                    )


urlpatterns = [
    path('list/', –°oursesListApiView.as_view(), name='list'),
    path('cat_list/', CategoryListApiView.as_view(), name='list'),
    path('cart/<int:id>/', GetCartAPIView.as_view(), name='cart'),

    path('create/', CoursesCreateAPIView.as_view(), name='create'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat_create'),
    path('filter/price/<int:price>/', FilterPrice.as_view(), name='filter_price'),
    path('filter/<slug:name>/', FilterByCategory.as_view(), name='filter'),
    path('filter/<slug:name>/<int:price>/', FilterCategoryByPrice.as_view(), name='filter_category_price'),

    path('add/to/car/', CreateCourseAPIView.as_view(), name='add_to_car'),
]