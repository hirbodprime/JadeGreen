from django.urls import path
from . import views as v
from rest_framework.authtoken.views import obtain_auth_token 
# from django.contrib.auth import views as auth_views
# from django.views.generic.base import RedirectView

urlpatterns = [
    path('APIlogin/', v.login_userview, name="loginusertest"),
    path('APIregister/', v.register_userview, name="registeruserview"),
    path('APIlogout/',v.logout_userview,name='logoutest'),
    # path('loginClassBased/',auth_views.LoginView.as_view(template_name="JadeUsers/login.html",redirect_authenticated_user = True),name='login'),
    path('login/' , v.loginView , name="loginviewname"),
    path('register/' , v.registerView, name="registerviewname"),
    path('api/userdetail/<int:pk>/' , v.DetailUsersAPIView.as_view()),
    # path('api/register/' , v.CreateUserAPIView.as_view()),
    path('api/userslist/' , v.ListUsersAPIView.as_view()),
    # path('api/login/' , v.login_user , name="loginview"),
    # path('api/logout/' , v.UserLogout , name="logoutview"),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


]