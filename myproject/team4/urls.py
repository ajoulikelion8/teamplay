from django.urls import path
from team4 import views

urlpatterns = [
    path('', views.team4, name = "team4"),
]
