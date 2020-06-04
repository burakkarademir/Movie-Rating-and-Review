from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    allMovies = Movie.objects.all()
 
    context = {
        "movies": allMovies,
    }

    return render(request, 'main/index.html', context)

# detail page

def detail(request, id):
    movie = Movie.objects.get(movie_id=id)

    context = {
        "movie": movie
    }
    return render(request, 'main/details.html', context)


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = MovieForm()
    return render(request, 'main/addmovies.html', {"form": form})


def addInfo(request, id):
    movie = Movie.objects.get(id=id)

    context = {
        "movie": movie
    }
    return render(request, 'main/add_info.html', context)

def add_release_date(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = ReleaseDateForm(request.POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            data.movie_id.add(movie)
            return redirect("main:home")
    else:
        form = ReleaseDateForm()
    return render(request, 'main/add_release_date.html', {"form": form})