from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="details"),
    path('addmovies/', views.add_movie, name="add_movie"),
    path('addreview/<int:id>/', views.addReview, name="add_review"),
    path('addreleasedate/<int:id>/', views.add_release_date, name="add_release_date")
    # path('add_info/<int:id>/', views.addInfo, name="add_info")
    path('/addreleasedate/<int:id>/', views.add_release_date, name="add_release_date"),
]
