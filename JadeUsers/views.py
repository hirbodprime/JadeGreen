from rest_framework import generics as gn
from django.contrib.auth import get_user_model , login , logout
from .serializers import UserSerializer , DetailUserSerializer , LoginSerializer
from rest_framework import views , status
from rest_framework.response import Response 
from rest_framework.decorators import api_view , permission_classes
from rest_framework import permissions as p


UserModel = get_user_model()



class CreateUserAPIView(gn.CreateAPIView):
    model = UserModel
    permission_classes = [p.AllowAny]
    serializer_class = UserSerializer



class ListUsersAPIView(gn.ListAPIView):
    permission_classes = [p.AllowAny]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class DetailUsersAPIView(gn.ListAPIView):
    permission_classes = [p.AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = DetailUserSerializer
    def get_queryset(self):
        return UserModel.objects.filter(id = self.kwargs['pk'])


    