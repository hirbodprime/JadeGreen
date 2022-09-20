from django.shortcuts import render
from .models import BlogModel
from .serializers import BlogModelSerializer
from rest_framework.generics import ListAPIView


class BlogListViewApi(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer




    