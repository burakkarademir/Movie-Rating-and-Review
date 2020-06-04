from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="details"),
    path('addmovies/', views.add_movie, name="add_movie"),
    path('addreview/<int:id>/', views.addReview, name="add_review"),
    path('addreleasedate/<int:id>/', views.add_release_date, name="add_release_date"),
    path('addsoundtrack/<int:id>/', views.add_soundtrack, name="add_soundtrack"),
    path('addkeywords/<int:id>/', views.add_keywords, name="add_keywords"),
    path('addcountry/<int:id>/', views.add_country, name="add_country"),
    path('addrating/<int:id>/', views.addRating, name="add_rating"),
    path('editreview/<int:movie_id>/<int:review_id>/', views.edit_review, name="edit_review")
    # path('add_info/<int:id>/', views.addInfo, name="add_info")
]
