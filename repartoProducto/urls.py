from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuenta/', include('django.contrib.auth.urls')),  # login y logout
    path('', include('app.urls')),  # Incluye las URLs de tu aplicación
]

