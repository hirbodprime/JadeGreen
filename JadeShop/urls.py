from django.urls import path
from .views import ProductListViewApi , ProductDetailViewApi

urlpatterns = [
    path('' , ProductListViewApi.as_view()),
    path('<int:id>' , ProductDetailViewApi.as_view()),
]