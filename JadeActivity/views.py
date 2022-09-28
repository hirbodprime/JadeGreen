from django.shortcuts import render
from .models import ActivitiesModel
from .serializers import ActivitiesModelSerializers
from rest_framework.generics import ListAPIView
from rest_framework import permissions as p


class ActivitiesListViewApi(ListAPIView):
    permission_classes = [p.AllowAny]
    queryset = ActivitiesModel.objects.all()
    serializer_class = ActivitiesModelSerializers

