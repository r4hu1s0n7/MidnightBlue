from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class MovieDB(models.Model):
    genres = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=100)
    keywords = models.CharField(max_length=500)
    original_title = models.CharField(max_length=100)
    overview = models.CharField(max_length=1000)
    popularity = models.FloatField()
    release_date = CharField(max_length=50)
    runtime = models.FloatField()
    tagline = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    cast = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    poster = models.CharField(max_length=1000)

    class Meta:
        db_table = "MovieDB"