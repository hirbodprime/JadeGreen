from django.urls import path
from .views import ActivitiesListViewApi

urlpatterns = [

    path('api/' , ActivitiesListViewApi.as_view())
]