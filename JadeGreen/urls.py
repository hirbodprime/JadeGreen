from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', include("JadeHome.urls")),
    path('admin/', admin.site.urls),
    path('shop/' , include('JadeShop.urls')),
    path('blog/' , include('JadeBlog.urls')),
    path('activity/' , include('JadeActivity.urls')),
    path('users/' , include('JadeUsers.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

