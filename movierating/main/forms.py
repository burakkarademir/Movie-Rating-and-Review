from django import forms
from .models import *


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'budget', 'runtime', 'avg_rank', 'summary', 'revenue', 'language', 'image')


class ReleaseDateForm(forms.ModelForm):
    class Meta:
        model = release_dates
        fields = ('country', 'release_date')