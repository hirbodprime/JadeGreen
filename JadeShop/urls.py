from django.urls import path
from .views import ProductListViewApi , ProductDetailViewApi

urlpatterns = [
    path('api/' , ProductListViewApi.as_view()),
    path('api/<int:id>/' , ProductDetailViewApi.as_view()),
]