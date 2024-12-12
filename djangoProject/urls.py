from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('security/', include('security.urls')),
    path('dette/', include('dette.urls')),
    path('budget/', include('budget.urls')),
]
