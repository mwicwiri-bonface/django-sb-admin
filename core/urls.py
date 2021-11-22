
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('sb_admin.urls', 'sb_admin'), namespace="sb_admin")),
]
