from django.urls import path
from .views import BookListView, GenreListView, AuthorListView, BookCreateView, BookDeleteView, BookUpdateView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
]    
