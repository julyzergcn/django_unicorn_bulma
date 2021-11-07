
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('components/', include('django_unicorn.urls')),
    path('', include('core.urls', namespace='core')),
]
