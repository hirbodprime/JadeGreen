from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('JadeShop/' , include('JadeShop.urls')),
    path('JadeBlog/' , include('JadeBlog.urls')),
    path('JadeActivity/' , include('JadeActivity.urls')),
    path('JadeUsers/' , include('JadeUsers.urls')),
]
