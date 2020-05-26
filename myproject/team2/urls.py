from django.urls import path
from team2 import views
import team2.views

urlpatterns = [
    path('', views.team2, name = "team2"),
    path('Juyeon/', views.Juyeon, name ="Juyeon"),
]
