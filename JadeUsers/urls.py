from django.urls import path
from . import views as v
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('login/' , v.loginView , name="loginviewname"),
    path('register/' , v.registerView, name="registerviewname"),
    path('api/userdetail/<int:pk>/' , v.DetailUsersAPIView.as_view()),
    path('api/register/' , v.CreateUserAPIView.as_view()),
    path('api/userslist/' , v.ListUsersAPIView.as_view()),
    path('api/login/' , v.login_user , name="loginview"),
    path('api/logout/' , v.UserLogout , name="logoutview"),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


]