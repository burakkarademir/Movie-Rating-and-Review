from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(review)
admin.site.register(ratings)
admin.site.register(release_dates)
admin.site.register(soundtrack)
admin.site.register(movie_soundtrack)
admin.site.register(production_company)
admin.site.register(production)
admin.site.register(award_name)
admin.site.register(category_name)
admin.site.register(awards)
admin.site.register(person)
admin.site.register(gender)
admin.site.register(character_role)
admin.site.register(movie_cast)
admin.site.register(departments)
admin.site.register(movie_crew)
admin.site.register(keywords)
admin.site.register(movie_keywords)
admin.site.register(country_name)
admin.site.register(countries)
admin.site.register(genres)
admin.site.register(movie_genre)