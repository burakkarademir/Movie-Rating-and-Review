from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300, default='')
    budget = models.IntegerField(null=True)
    runtime = models.IntegerField(null=True)
    avg_rank = models.FloatField(null=True)
    # count_rank = models.IntegerField(null=True)
    summary = models.TextField(max_length=5000, default='')
    revenue = models.IntegerField(null=True)
    language = models.CharField(max_length=300, default='')
    image = models.URLField(default=None, null=True)

    def __str__(self):
        return self.title


class release_dates(models.Model):
    movie_id = models.ManyToManyField(Movie)
    country = models.CharField(max_length=300, default='')
    release_date = models.CharField(max_length=300, default='')


class genres(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=300, default='')


class movie_genre(models.Model):
    movie_id = models.ManyToManyField(Movie)
    genre_id = models.OneToOneField(
        genres,
        on_delete=models.CASCADE,
    )


class person(models.Model):
    person_id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=300, default='')
    person_lastname = models.CharField(max_length=300, default='')
    person_birthdate = models.DateField()
    person_deathdate = models.DateField()


class gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=300, default='')


class movie_cast(models.Model):
    movie_id = models.ManyToManyField(Movie)
    person_id = models.OneToOneField(
        person,
        on_delete=models.CASCADE,
    )
    gender_id = models.OneToOneField(
        gender,
        on_delete=models.CASCADE,
    )
    character_name = models.CharField(max_length=300, default='')
    character_order = models.IntegerField()


class character_role(models.Model):
    movie_id = models.ManyToManyField(Movie)
    person_id = models.ForeignKey(person, on_delete=models.CASCADE)
    role = models.CharField(max_length=300, default='')


class departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=300, default='')


class movie_crew(models.Model):
    movie_id = models.ManyToManyField(Movie)
    department_id = models.OneToOneField(
        departments,
        on_delete=models.CASCADE,
    )
    person_id = models.ForeignKey(person, on_delete=models.CASCADE)
    job = models.CharField(max_length=300, default='')


class production(models.Model):
    production_id = models.AutoField(primary_key=True)
    production_name = models.CharField(max_length=300, default='')


class production_company(models.Model):
    movie_id = models.ManyToManyField(Movie)
    production_id = models.OneToOneField(
        production,
        on_delete=models.CASCADE,
    )


class award_name(models.Model):
    award_id = models.AutoField(primary_key=True)
    award_name = models.CharField(max_length=300, default='')


class category_name(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=300, default='')


class awards(models.Model):
    movie_id = models.ManyToManyField(Movie)
    award_id = models.OneToOneField(
        award_name,
        on_delete=models.CASCADE,
    )
    category_id = models.OneToOneField(
        category_name,
        on_delete=models.CASCADE,
    )
    year = models.DateField()


class review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField(max_length=5000)

    def __str__(self):
        return self.user_id.username


class ratings(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ManyToManyField(Movie)
    rating = models.FloatField()


class country_name(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=300, default='')


class countries(models.Model):
    movie_id = models.ManyToManyField(Movie)
    country_id = models.OneToOneField(
        country_name,
        on_delete=models.CASCADE,
    )


class keywords(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword_name = models.CharField(max_length=300, default='')


class movie_keywords(models.Model):
    movie_id = models.ManyToManyField(Movie)
    keyword_id = models.OneToOneField(
        keywords,
        on_delete=models.CASCADE,
    )


class soundtrack(models.Model):
    soundtrack_id = models.AutoField(primary_key=True)
    soundtrack_name = models.CharField(max_length=300, default='')
    writer_name = models.CharField(max_length=300, default='')
    singer = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.soundtrack_name


class movie_soundtrack(models.Model):
    movie_id = models.ManyToManyField(Movie)
    soundtrack_id = models.OneToOneField(
        soundtrack,
        on_delete=models.CASCADE,
    )


def __str__(self):
    return self.name


def __unicode__(self):
    return self.name
