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
    reviews = review.objects.filter(movie_id=id)

    context = {
        "movie": movie,
        "reviews": reviews
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


def addReview(request, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(movie_id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.review = request.POST["review"]
                data.user_id = request.user
                data.movie_id = movie
                data.save()
                return redirect("main:home")
        else:
            form = ReviewForm()
        return render(request, 'main/index.html', {"form": form})
    else:
        return redirect("main:home")


def addRating(request, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(movie_id=id)
        if request.method == "POST":
            form = RatingForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.user_id = request.user
                if ratings.objects.filter(user_id=request.user).exists() is False:
                    if (data.rating <= 10) or (data.rating > 0):
                        data.save()
                        data.movie_id.add(movie)
                        x = ratings.objects.filter(movie_id=movie).all()
                        y = 0
                        count = 0
                        for i in x:
                            y = y + i.rating
                            count = count+1
                        avgR = y/count
                        Movie.objects.filter(movie_id=id).update(avg_rank=avgR)
                        return redirect("main:home")
                    else:
                        error = "Out of range. Select a rating between 0 and 10."
                        return render(request, 'main/add_rating.html', {"error": error, "form": form})
                else:
                    error = "You can't rate the same movie more than once."
                    return render(request, 'main/add_rating.html', {"error": error, "form": form})
        else:
            form = RatingForm()
        return render(request, 'main/add_rating.html', {"form": form})
    else:
        return redirect("main:home")


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


def add_soundtrack(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = SoundtrackForm(request.POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            st = soundtrack.objects.get(soundtrack_name=data.soundtrack_name)
            ms = movie_soundtrack(soundtrack_id=st)
            ms.save()
            ms.movie_id.add(movie)
            return redirect("main:home")
    else:
        form = SoundtrackForm()
    return render(request, 'main/add_soundtrack.html', {"form": form})


def add_keywords(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = KeywordsForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            kw = keywords.objects.get(keyword_name=data.keyword_name)
            mk = movie_keywords(keyword_id=kw)
            mk.save()
            mk.movie_id.add(movie)
            return redirect("main:home")
    else:
        form = KeywordsForm()
    return render(request, 'main/add_keywords.html', {"form": form})


def add_country(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = CountryNameForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            ct = country_name.objects.get(country_name=data.country_name)
            cts = countries(country_id=ct)
            cts.save()
            cts.movie_id.add(movie)
            return redirect("main:home")
    else:
        form = CountryNameForm()
    return render(request, 'main/add_country.html', {"form": form})


def edit_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(movie_id=movie_id)
        Review = review.objects.get(movie_id=movie, id=review_id)

        if request.user == Review.user_id:
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=Review)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:details", movie_id)
            else:
                form = ReviewForm(instance=Review)
            return render(request, 'main/edit_review.html', {"form": form})
        else:
            return redirect("main:details", movie_id)
    else:
        return redirect("main:home")
