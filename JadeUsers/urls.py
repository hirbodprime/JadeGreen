from django.urls import path
from . import views as v
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('Login/' , v.loginView , name="loginviewname"),
    path('Register/' , v.registerView, name="registerviewname"),
    path('UserDetail/<int:pk>/' , v.DetailUsersAPIView.as_view()),
    path('register/' , v.CreateUserAPIView.as_view()),
    path('UsersList/' , v.ListUsersAPIView.as_view()),
    path('login/' , v.login_user , name="loginview"),
    path('logout/' , v.UserLogout , name="logoutview"),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


]