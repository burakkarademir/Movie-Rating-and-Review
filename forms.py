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

class ProductionForm(forms.ModelForm):
    class Meta:
        model = production
        fields = ('production_name',)


class AwardForm(forms.ModelForm):
    class Meta:
        model = award_name
        fields = ('award_name', 'year')


class AwardCategoryForm(forms.ModelForm):
    class Meta:
        model = category_name
        fields = ('category_name',)


class PersonForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ('person_name', 'person_lastname', 'person_birthdate', 'person_deathdate')


class RoleForm(forms.ModelForm):
    class Meta:
        model = character_role
        fields = ('role', 'character_name', 'character_order')


class GenderForm(forms.ModelForm):
    class Meta:
        model = gender
        fields = ('gender',)


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = departments
        fields = ('department_name', 'job')


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