from django.urls import path
from .views import BlogListViewApi

urlpatterns = [
    path('' , BlogListViewApi.as_view())
]