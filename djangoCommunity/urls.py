from django.contrib import admin
from django.urls import path, include
from users.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('board/', include('board.urls')),
    path('', home),
]
