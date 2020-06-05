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
    rds = release_dates.objects.filter(movie_id=id)

    # country section
    ct = countries.objects.filter(movie_id=movie)
    ct_list = []
    for j in ct:
        ctx = j.country_id
        ct_list.append(ctx)
    
    # production section
    pd = production_company.objects.filter(movie_id=movie)
    pd_list = []
    for l in pd:
        pdx = l.production_id
        pd_list.append(pdx)
    
    # key words section
    kw = movie_keywords.objects.filter(movie_id=movie)
    kw_list = []
    for i in kw:
        kwx = i.keyword_id
        kw_list.append(kwx)

    #soundtrack section
    soundtrack2 = movie_soundtrack.objects.filter(movie_id=movie)
    soundtracks = []
    for i in soundtrack2:
        soundtrack_name=i.soundtrack_id
        soundtracks.append(soundtrack_name)

    # genre section
    genre = movie_genre.objects.filter(movie_id=movie)
    genre_list = []
    for i in genre:
        kwx = i.genre_id
        genre_list.append(kwx)


    # award section
    award = awards.objects.filter(movie_id=movie)
    award_dict = {}
    count = 0
    for i in award:
        award_dict[award[count].award_id] = award[count].category_id
        count = count +1

    # cast section
    cast = movie_cast.objects.filter(movie_id=movie)
    cast_list = []
    for j in cast:
        cast_list.append(j)

    # crew section
    crew = movie_crew.objects.filter(movie_id=movie)
    crew_list = []
    for j in crew:
        crew_list.append(j)

    context = {
        "movie": movie,
        "reviews": reviews,
        "keywords": kw_list,
        "soundtrack": soundtracks,
        "country": ct_list,
        "release_dates": rds,
        "genres": genre_list,
        "productions": pd_list,
        "awards": award_dict,
        "cast": cast_list,
        "crew": crew_list
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
                if ratings.objects.filter(user_id=request.user, movie_id=movie).exists() is False:
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
            if release_dates.objects.filter(movie_id=movie, country=data.country, release_date=data.release_date).exists() is True:
                error = "This entry already exists! Try again with a new one."
                return render(request, 'main/add_release_date.html', {"error": error, "form": form})
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
            st = soundtrack.objects.latest('soundtrack_id')
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
            y = movie_keywords.objects.filter(movie_id=movie)
            y_value = False
            for j in y:
                yx = j.keyword_id
                if (yx.keyword_name == data.keyword_name):
                    error = "This entry already exists! Try again with a new one."
                    return render(request, 'main/add_keywords.html', {"error": error, "form": form})
            data.save()
            kw = keywords.objects.latest('keyword_id')
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
            y = countries.objects.filter(movie_id=movie)
            y_value = False
            for j in y:
                yx = j.country_id
                if (yx.country_name == data.country_name):
                    error = "This entry already exists! Try again with a new one."
                    return render(request, 'main/add_country.html', {"error": error, "form": form})
            data.save()
            ct = country_name.objects.latest('country_id')
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


def delete_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(movie_id=movie_id)
        Review = review.objects.get(movie_id=movie, id=review_id)

        if request.user == Review.user_id:
            Review.delete()
        
        return redirect("main:details", movie_id)
    else:
        return redirect("main:home")


def edit_keywords(request, movie_id, key_id):
    movie = Movie.objects.get(movie_id=movie_id)
    # kid = movie_keywords.objects.get(movie_id=movie)
    kinfo = keywords.objects.get(keyword_id=key_id)
    if request.method == "POST":
        form = KeywordsForm(request.POST or None, instance=kinfo)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:details", movie_id)
    else:
        form = KeywordsForm(instance=kinfo)
    return render(request, 'main/edit_keywords.html', {"form": form})


def add_production(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = ProductionForm(request.POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            y = production_company.objects.filter(movie_id=movie)
            y_value = False
            for j in y:
                yx = j.production_id
                if (yx.production_name == data.production_name):
                    error = "This entry already exists! Try again with a new one."
                    return render(request, 'main/add_production.html', {"error": error, "form": form})
            data.save()
            production_object = production.objects.latest('production_id')
            company = production_company(production_id=production_object)
            company.save()
            company.movie_id.add(movie)
            return redirect("main:home")
    else:
        form = ProductionForm()
    return render(request, 'main/add_production.html', {"form": form})


def add_award_and_category(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = AwardForm(request.POST or None)
        form2 = AwardCategoryForm(request.POST or None)

        if form.is_valid() and form2.is_valid():
            data = form.save(commit=False)
            data2 = form2.save(commit=False)
            if (award_name.objects.filter(award_name=data.award_name, year=data.year).exists() and category_name.objects.filter(category_name=data2.category_name).exists()) is True:
                error = "This entry already exists! Try again with a new one."
                return render(request, 'main/add_award_category.html', {"error": error, "form": form, "form2": form2})
            data2.save()
            data.save()
            award = award_name.objects.latest('award_id')
            category = category_name.objects.latest('category_id')
            awardss = awards(award_id=award ,category_id=category)
            awardss.save()
            awardss.movie_id.add(movie)
            return redirect("main:home")
    else:
        form = AwardForm()
        form2 = AwardCategoryForm()

    return render(request, 'main/add_award_category.html', {"form": form, "form2": form2})


def add_movie_cast(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = PersonForm(request.POST or None)
        form2 = RoleForm(request.POST or None)
        form3 = GenderForm(request.POST or None)

        if form.is_valid() and form2.is_valid() and form3.is_valid():
            data = form.save(commit=False)
            data2 = form2.save(commit=False)
            data3 = form3.save(commit=False)
            data3.save()
            data2.save()
            data.save()
            person_info = person.objects.latest('person_id')
            character_info = character_role.objects.latest('character_id')
            gender_info = gender.objects.latest('gender_id')
            cast_detail = movie_cast(person_id=person_info, gender_id=gender_info, character_id=character_info)
            cast_detail.save()
            cast_detail.movie_id.add(movie)
            return redirect("main:home")
    else:
        form = PersonForm()
        form2 = RoleForm()
        form3 = GenderForm()

    return render(request, 'main/add_movie_cast.html', {"form": form, "form2": form2, "form3": form3})


def add_movie_crew(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = PersonForm(request.POST or None)
        form2 = DepartmentForm(request.POST or None)

        if form.is_valid() and form2.is_valid():
            data = form.save(commit=False)
            data2 = form2.save(commit=False)
            data2.save()
            data.save()
            person_info = person.objects.latest('person_id')
            department_info = departments.objects.latest('department_id')
            crew_info = movie_crew(department_id=department_info, person_id=person_info)
            crew_info.save()
            crew_info.movie_id.add(movie)
            return redirect("main:home")
    else:
        form = PersonForm()
        form2 = DepartmentForm()

    return render(request, 'main/add_movie_crew.html', {"form": form, "form2": form2})


def edit_movie(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = MovieForm(request.POST or None, instance=movie)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:details", id)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'main/edit_movies.html', {"form": form})


def delete_movie(request, id):
    movie = Movie.objects.get(movie_id=id)
    movie.delete()
    return redirect("main:home")


def edit_release_date(request, id):
    movie = Movie.objects.get(movie_id=id)
    release = release_dates.objects.get(movie_id=movie.movie_id)
    if request.method == "POST":
        form = ReleaseDateForm(request.POST or None, instance=release)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = ReleaseDateForm(instance=release)
    return render(request, 'main/edit_release_date.html', {"form": form})


def edit_soundtrack(request, movie_id, key_id):
    movie = Movie.objects.get(movie_id=movie_id)
    # soundtrackid = movie_soundtrack.objects.get(movie_id=movie)
    soundtrack_info = soundtrack.objects.get(soundtrack_id=key_id)
    if request.method == "POST":
        form = SoundtrackForm(request.POST or None, instance=soundtrack_info)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = SoundtrackForm(instance=soundtrack_info)
    return render(request, 'main/edit_soundtrack.html', {"form": form})


def edit_country(request, movie_id, key_id):
    movie = Movie.objects.get(movie_id=movie_id)
    # cid = countries.objects.get(movie_id=movie)
    cinfo = country_name.objects.get(country_id=key_id)
    if request.method == "POST":
        form = CountryNameForm(request.POST or None, instance=cinfo)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:details", movie_id)
    else:
        form = CountryNameForm(instance=cinfo)
    return render(request, 'main/edit_country.html', {"form": form})


def add_genre(request, id):
    movie = Movie.objects.get(movie_id=id)
    if request.method == "POST":
        form = GenreForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            y = movie_genre.objects.filter(movie_id=movie)
            y_value = False
            for j in y:
                yx = j.genre_id
                if (yx.genre == data.genre):
                    error = "This entry already exists! Try again with a new one."
                    return render(request, 'main/add_genre.html', {"error": error, "form": form})
            data.save()
            kw = genres.objects.latest('genre_id')
            mk = movie_genre(genre_id=kw)
            mk.save()
            mk.movie_id.add(movie)
            return redirect("main:home")
    else:
        form = GenreForm()
    return render(request, 'main/add_genre.html', {"form": form})


def edit_genre(request, movie_id, key_id):
    movie = Movie.objects.get(movie_id=movie_id)
    # kid = movie_keywords.objects.get(movie_id=movie)
    genre = genres.objects.get(genre_id=key_id)
    if request.method == "POST":
        form = GenreForm(request.POST or None, instance=genre)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:details", movie_id)
    else:
        form = GenreForm(instance=genre)
    return render(request, 'main/edit_genre.html', {"form": form})


def edit_award_and_category(request, movie_id, award_id, category_id):
    movie = Movie.objects.get(movie_id=movie_id)
    # kid = movie_keywords.objects.get(movie_id=movie)
    awardd = award_name.objects.get(award_id=award_id)
    categry = category_name.objects.get(category_id=category_id)
    if request.method == "POST":
        form = AwardForm(request.POST or None, instance=awardd)
        form2 = AwardCategoryForm(request.POST or None, instance=categry)

        if form.is_valid():
            data = form.save(commit=False)
            data2 = form2.save(commit=False)
            data2.save()
            data.save()
            return redirect("main:details", movie_id)
    else:
        form = AwardForm(instance=awardd)
        form2 = AwardCategoryForm(instance=categry)
    return render(request, 'main/edit_award_category.html', {"form": form, "form2": form2})


def delete_keywords(request, id, key_id):
    movie = Movie.objects.get(movie_id=id)
    keyword = movie_keywords.objects.get(movie_id=movie, keyword_id=key_id)
    keyword.delete()
    return redirect("main:home")


def delete_award_and_category(request, movie_id, award_id, category_id):
    movie = Movie.objects.get(movie_id=movie_id)
    awardd = awards.objects.get(movie_id=movie, award_id=award_id, category_id=category_id)
    awardd.delete()
    return redirect("main:home")


def delete_genre(request, movie_id, key_id):
    movie = Movie.objects.get(movie_id=movie_id)
    genre = genres.objects.get(genre_id=key_id)
    genre.delete()
    return redirect("main:home")


def delete_soundtrack(request, movie_id, soundtrack_id):
    movie = Movie.objects.get(movie_id=movie_id)
    soundtrack_info = soundtrack.objects.get(soundtrack_id=soundtrack_id)
    soundtrack_info.delete()
    return redirect("main:home")


def delete_country(request, movie_id, key_id):
    movie = Movie.objects.get(movie_id=movie_id)
    ct = country_name.objects.get(country_id=key_id)
    ct.delete()
    return redirect("main:home")


def delete_release_date(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    rd = release_dates.objects.get(movie_id=movie)
    rd.delete()
    return redirect("main:home")

def delete_production(request, movie_id, key_id):
    movie = Movie.objects.get(movie_id=movie_id)
    pd = production.objects.get(production_id=key_id)
    pd.delete()
    return redirect("main:home")
def delete_movie_cast(request, movie_id, character_id, person_id, gender_id):
    movie = Movie.objects.get(movie_id=movie_id)
    cast = movie_cast.objects.get(movie_id=movie, character_id=character_id, person_id=person_id, gender_id=gender_id)
    cast.delete()
    return redirect("main:home")


def delete_movie_crew(request, movie_id, person_id, department_id):
    movie = Movie.objects.get(movie_id=movie_id)
    crew = movie_crew.objects.get(movie_id=movie, person_id=person_id, department_id=department_id)
    crew.delete()
    return redirect("main:home")
    
