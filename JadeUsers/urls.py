from django.urls import path
from .views import CreateUserAPIView , DetailUsersAPIView,ListUsersAPIView 

urlpatterns = [
    path('UserDetail/<int:pk>/' , DetailUsersAPIView.as_view()),
    path('register/' , CreateUserAPIView.as_view()),
    path('UsersList/' , ListUsersAPIView.as_view()),

]