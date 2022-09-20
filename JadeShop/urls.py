from django.urls import path
from .views import ProductListViewApi

urlpatterns = [
    path('' , ProductListViewApi.as_view())
]