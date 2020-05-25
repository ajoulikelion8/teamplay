
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp', include('myapp.urls')),
    path('team1', include('team1.urls')),
    path('team2', include('team2.urls')),
    path('team3', include('team3.urls')),
    path('team4', include('team4.urls')),
]
