from rest_framework import serializers
from django.contrib.auth import get_user_model 
from django.utils import timezone


UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    # date_joined = serializers.DateTimeField(read_only=True)
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            password2=validated_data['password2'],
        )
        return user
        
    def validate(self, data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data
    class Meta:
        model = UserModel
        fields = ( "id", "username","email", "password", "password2")


class DetailUserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    fullname = serializers.CharField(read_only=True)
    class Meta:
            model = UserModel
            fields = ( "id", "username","first_name" , "last_name","email",'fullname',"date_joined")