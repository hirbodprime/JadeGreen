from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import ProductModel
from .serializers import ProductModelSerializer


class ProductListViewApi(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


