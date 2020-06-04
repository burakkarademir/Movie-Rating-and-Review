from django import forms
from .models import *


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'budget', 'runtime', 'avg_rank', 'summary', 'revenue', 'language', 'image')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ('review',)


class ReleaseDateForm(forms.ModelForm):
    class Meta:
        model = release_dates
        fields = ('country', 'release_date')
class ReleaseDateForm(forms.ModelForm):
    class Meta:
        model = release_dates
        fields = ('country', 'release_date')
