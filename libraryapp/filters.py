import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')
    authors = django_filters.CharFilter(field_name="authors__name", lookup_expr='icontains')
    published_year_min = django_filters.NumberFilter(field_name="published_year", lookup_expr='gte')
    published_year_max = django_filters.NumberFilter(field_name="published_year", lookup_expr='lte')
    published_year = django_filters.NumberFilter(field_name="published_year", lookup_expr='exact')
    
    class Meta:
        model = Book
        fields = ['title', 'genre', 'authors', 'published_year_min', 'published_year_max']