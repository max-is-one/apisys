from django.urls import path
from .views import ParseBooksView, ExportBooksView

urlpatterns = [
    path('parse-books/', ParseBooksView.as_view(), name='parse-books'),
    path('export-books/', ExportBooksView.as_view(), name='export-books'),
]