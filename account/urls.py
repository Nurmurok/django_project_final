from django.urls import path

from .views import (
RegisterAPIView,
MyObtainPairView,
UserListView,
UserDetailApiView,
UserDestroyApiView
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', MyObtainPairView.as_view(), name='login'),
    path('list/', UserListView.as_view(), name='list'),
    path('detail/', UserDetailApiView.as_view(), name='login'),
    path('delete/', UserDestroyApiView.as_view(), name='login'),
]