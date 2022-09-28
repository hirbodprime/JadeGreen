from django.shortcuts import render
from .models import BlogModel
from .serializers import BlogModelSerializer
from rest_framework.generics import ListAPIView
from rest_framework import permissions as p

class BlogListViewApi(ListAPIView):
    permission_classes = [p.AllowAny]
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer




    