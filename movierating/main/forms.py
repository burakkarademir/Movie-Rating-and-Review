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


class SoundtrackForm(forms.ModelForm):
    class Meta:
        model = soundtrack
        fields = ('soundtrack_name', 'writer_name', 'singer')


class KeywordsForm(forms.ModelForm):
    class Meta:
        model = keywords
        fields = ('keyword_name',)


class CountryNameForm(forms.ModelForm):
    class Meta:
        model = country_name
        fields = ('country_name',)


class RatingForm(forms.ModelForm):
    class Meta:
        model = ratings
        fields = ('rating',)
