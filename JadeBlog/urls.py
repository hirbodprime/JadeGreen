from django.urls import path
from .views import BlogListViewApi

urlpatterns = [
    path('api/' , BlogListViewApi.as_view())
]