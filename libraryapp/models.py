from django.db import models
from .mixins import TimeStampedUUIDModel

# Create your models here.

class Author(TimeStampedUUIDModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(TimeStampedUUIDModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(TimeStampedUUIDModel):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default="Unknown")
    published_year = models.IntegerField()

    def __str__(self):
        return self.title