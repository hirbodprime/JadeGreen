from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import ProductModel
from .serializers import ProductListModelSerializer , ProductDetailModelSerializer


class ProductListViewApi(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductListModelSerializer


class ProductDetailViewApi(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductDetailModelSerializer
    def get_queryset(self):
        return ProductModel(ProductModel.objects.filter(id = self.kwargs["id"]))


