from django.urls import path
from team3 import views

urlpatterns = [
    path('', views.team3, name = "team3"),
]
