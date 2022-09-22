from rest_framework import serializers
from .models import ProductModel



class ProductListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id','name','price' , 'offer')


class ProductDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id','name' ,'discription','price' , 'offer')