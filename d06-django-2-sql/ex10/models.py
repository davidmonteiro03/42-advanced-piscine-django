from django.db import models

# Create your models here.
class Planets(models.Model):
    name = models.CharField(unique=True,
                            max_length=64,
                            null=False)
    climate = models.CharField(null=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.CharField(max_length=128,
                               null=True)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=64,
                            null=False)
    birth_year = models.CharField(max_length=32,
                                  null=True)
    gender = models.CharField(max_length=32,
                              null=True)
    eye_color = models.CharField(max_length=32,
                                 null=True)
    hair_color = models.CharField(max_length=32,
                                  null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey(to=Planets,
                                  on_delete=models.CASCADE,
                                  null=True)

    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(unique=True,
                             max_length=64,
                             null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32,
                                null=False)
    producer = models.CharField(max_length=128,
                                null=False)
    release_date = models.DateField(null=False)
    characters = models.ManyToManyField(to=People,
                                        null=False,
                                        through='MoviesCharacters')

    def __str__(self):
        return self.title


class MoviesCharacters(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    character = models.ForeignKey(People, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('movie', 'character')
