from rest_framework import permissions as p
from rest_framework import generics as gn
from django.contrib.auth import get_user_model
from .serializers import UserSerializer , DetailUserSerializer

UserModel = get_user_model()

class CreateUserAPIView(gn.CreateAPIView):
    model = UserModel
    permission_classes = [p.AllowAny]
    serializer_class = UserSerializer



class ListUsersAPIView(gn.ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    # permission_classes = [p.IsAdminUser]

class DetailUsersAPIView(gn.ListAPIView):
    # permission_classes = [p.IsAdminUser]
    queryset = UserModel.objects.all()
    serializer_class = DetailUserSerializer
    
    def get_queryset(self):
        return UserModel.objects.filter(id = self.kwargs['pk'])


    