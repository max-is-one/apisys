from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Genre, Book
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer
from authapp.permissions import IsAdminUser
import django_filters

# Create your views here.

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')
    authors = django_filters.CharFilter(field_name="authors__name", lookup_expr='icontains')
    published_year_min = django_filters.NumberFilter(field_name="published_year", lookup_expr='gte')
    published_year_max = django_filters.NumberFilter(field_name="published_year", lookup_expr='lte')
    
    class Meta:
        model = Book
        fields = ['title', 'genre', 'authors', 'published_year_min', 'published_year_max']

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    ordering_fields = ['title', 'genre', 'authors__name', 'published_year']

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAdminUser]

class BookUpdateView(generics.UpdateAPIView): 
    queryset = Book.objects.all() 
    serializer_class = BookSerializer 
    permission_classes = [IsAdminUser]
