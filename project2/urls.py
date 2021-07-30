from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloapp.urls')),
    path('profile/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
