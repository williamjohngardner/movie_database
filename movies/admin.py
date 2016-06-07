from django.contrib import admin
from movies.models import Rating
from movies.models import Rater
from movies.models import Movie


admin.site.register([Rater, Rating, Movie])
