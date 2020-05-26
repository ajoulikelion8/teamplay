
from django.urls import path
from team1 import views

urlpatterns = [
    path('', views.team1, name = "team1"),
]
