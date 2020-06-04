from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(review)
admin.site.register(release_dates)