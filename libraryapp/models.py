from django.db import models
from .mixins import BaseModelMixin

# Create your models here.

class Author(BaseModelMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(BaseModelMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(BaseModelMixin):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default="Unknown")
    published_year = models.IntegerField()

    def __str__(self):
        return self.title