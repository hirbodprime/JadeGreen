from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import ProductModel
from .serializers import ProductListModelSerializer , ProductDetailModelSerializer
from rest_framework import permissions as p

class ProductListViewApi(ListAPIView):
    permission_classes = [p.AllowAny]
    queryset = ProductModel.objects.all()
    serializer_class = ProductListModelSerializer


class ProductDetailViewApi(ListAPIView):
    permission_classes = [p.AllowAny]
    queryset = ProductModel.objects.all()
    serializer_class = ProductDetailModelSerializer
    def get_queryset(self):
        return ProductModel.objects.filter(id = self.kwargs["id"])


