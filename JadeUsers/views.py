from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

UserModel = get_user_model()

class CreateUserView(CreateAPIView):
    model = UserModel
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer





    