from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField()
    movie_title = models.CharField(max_length=60)
    release_date = models.IntegerField()
    video_release_date = models.CharField(max_length=10, default="")
    IMDb_URL = models.URLField()
    unknown = models.BooleanField()
    action = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    childrens = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sci_fi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()


class Rater(models.Model):
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)


class Rating(models.Model):
    user_id = models.IntegerField()
    item_id = models.IntegerField()
    rating = models.IntegerField()
    timestamp = models.IntegerField()
    movie_id = models.ForeignKey(Movie)
    rater_id = models.ForeignKey(Rater)

