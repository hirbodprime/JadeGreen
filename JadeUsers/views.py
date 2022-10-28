from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model , authenticate , login , logout
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer , DetailUserSerializer 
from rest_framework import generics as gn
from rest_framework import permissions as p
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.validators import ValidationError
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import json
from django.contrib.auth.hashers import check_password


UserModel = get_user_model()

def registerView(req):
    return render(req , 'JadeUsers/SignUp.html')

def loginView(request):
    if request.user and request.user.is_authenticated:
        return redirect("homeviewname")
    return render(request , 'JadeUsers/login.html')

@api_view(["GET"])
@permission_classes([p.IsAuthenticated])
def UserLogout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully', status=HTTP_200_OK)



@api_view(["POST"])
@permission_classes([p.AllowAny])
def login_user(request):
        data = {}
        reqBody = json.loads(request.body)
        username = reqBody['username']
        # print(username)
        password = reqBody['password']
        try:
            Account = UserModel.objects.get(username=username)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})
        token = Token.objects.get_or_create(user=Account)[0].key
        # print(token)
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})
        if Account:
            if Account.is_active:
                print(request.user)
                login(request, Account)
                data["message"] = "user logged in"
                data["username"] = Account.username
                Res = {"data": data, "token": token}
                return Response(Res)
            else:
                raise ValidationError({"400": f'Account not active'})
        else:
            raise ValidationError({"400": f'Account doesnt exist'})

# test ------------------------------------------------------------

def login_userview(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
                print(resp)
                # return redirect("/")
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

def logout_userview(request):
    logout(request)
    return redirect('/')

def register_userview(request):
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    passwordRepeat = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        passwordRepeat = request.POST['passwordRepeat']
        user = UserModel.objects.create_user(username=username , password=password , password2=passwordRepeat)
        user = authenticate(username=username, password=password)
        if user is not None:
            # if user.is_active:
                login(request, user)
                resp['status']='success'
                print(resp)
                # return redirect("/")
            # else:
            #     resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')


class CreateUserAPIView(gn.CreateAPIView):
    model = UserModel
    permission_classes = [p.AllowAny]
    serializer_class = UserSerializer



class ListUsersAPIView(gn.ListAPIView):
    permission_classes = [p.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class DetailUsersAPIView(gn.ListAPIView):
    permission_classes = [p.AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = DetailUserSerializer
    def get_queryset(self):
        return UserModel.objects.filter(id = self.kwargs['pk'])


    