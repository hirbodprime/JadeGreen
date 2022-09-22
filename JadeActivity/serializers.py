from rest_framework import serializers
from .models import ActivitiesModel

class ActivitiesModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivitiesModel 
        fields = ('name' , 'discription')