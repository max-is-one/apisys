from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_set_books, books_to_excel

# Create your views here.

class ParseBooksView(APIView):
    def get(self, request):
        get_set_books()
        return Response({'message': 'Books parsed and saved successfully'}, status=status.HTTP_200_OK)


class ExportBooksView(APIView):
    def get(self, request):
        filter_params = {}
        if 'year' in request.query_params:
            filter_params['published_year'] = request.query_params.get('year')
        if 'year_from' in request.query_params:
            filter_params['published_year__gte'] = request.query_params['year_from']
        if 'year_to' in request.query_params:
            filter_params['published_year__lte'] = request.query_params['year_to']
        if 'author' in request.query_params:
            filter_params['authors__name__icontains'] = request.query_params['author']
        if 'genre' in request.query_params:
            filter_params['genre__name__icontains'] = request.query_params['genre']
        if 'title' in request.query_params:
            filter_params['title__icontains'] = request.query_params['title']
        return books_to_excel(filter_params)
