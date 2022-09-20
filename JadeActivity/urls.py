from django.urls import path
from .views import ActivitiesListViewApi

urlpatterns = [

    path('' , ActivitiesListViewApi.as_view())
]