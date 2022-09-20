from django.shortcuts import render
from .models import ActivitiesModel
from .serializers import ActivitiesModelSerializers
from rest_framework.generics import ListAPIView



class ActivitiesListViewApi(ListAPIView):
    queryset = ActivitiesModel.objects.all()
    serializer_class = ActivitiesModelSerializers

