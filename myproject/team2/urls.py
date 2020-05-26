from django.urls import path
from team2 import views

urlpatterns = [
    path('', views.team2, name = "team2"),
]
