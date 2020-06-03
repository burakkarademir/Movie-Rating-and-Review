from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="details"),
    path('addmovies/', views.add_movie, name="add_movie")
]
