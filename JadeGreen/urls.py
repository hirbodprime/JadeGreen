from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('JadeShop/' , include('JadeShop.urls')),
    path('JadeBlog/' , include('JadeBlog.urls')),
    path('JadeActivity/' , include('JadeActivity.urls')),
    path('JadeUsers/' , include('JadeUsers.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

