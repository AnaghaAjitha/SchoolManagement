from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin URLs
    path('api/', include('schoolSystem.urls')),  # Include URLs from the schoolSystem app
]
