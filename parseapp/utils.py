import requests
import pandas
import xlsxwriter
import io
from bs4 import BeautifulSoup
from libraryapp.models import Book, Author, Genre
from django.http import HttpResponse

def get_set_books(url = 'https://book24.ua/ua/catalog/skidki/'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    base_url = 'https://book24.ua'

    for book in soup.find_all('div', class_='item-title'):
        title = book.find('a', class_='dark_link option-font-bold font_sm').find('span').text.strip()
        book_url = book.find('a', class_='dark_link option-font-bold font_sm')['href']
        
        if not book_url.startswith('http'):
            book_url = base_url + book_url

        book_response = requests.get(book_url)
        book_soup = BeautifulSoup(book_response.content, 'html.parser')
        
        properties = book_soup.find_all('div', class_='properties__value darken properties__item--inline')

        authors = properties[0].find_all('a')
        author_instances = []
        for author in authors:
            author_name = author.text.strip()
            author_instance, created = Author.objects.get_or_create(name=author_name)
            author_instances.append(author_instance)

        genre_name = properties[3].text.strip()
        genre, created = Genre.objects.get_or_create(name=genre_name)

        year = properties[4].text.strip()
        year = int(year)
        book_instance, created = Book.objects.update_or_create(
            title=title,
            defaults={'genre': genre, 'published_year': year}
        )
        book_instance.authors.set(author_instances)
        


from django.http import HttpResponse
import io

def books_to_excel(filter_params=None):
    if filter_params is None:
        filter_params = {}
    books = Book.objects.filter(**filter_params)
    
    data = []
    for book in books:
        data.append({
            'Title': book.title,
            'Author': ', '.join([author.name for author in book.authors.all()]),
            'Genre': book.genre.name,
            'Year': book.published_year,
        })
    df = pandas.DataFrame(data)
    
    output = io.BytesIO()
    writer = pandas.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Books')
    
    workbook = writer.book
    worksheet = writer.sheets['Books']
    
    format_books = workbook.add_format({'num_format': '0'})
    worksheet.set_column('A:A', 50)
    worksheet.set_column('B:B', 40)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 8, format_books)
    
    writer.close()
    output.seek(0)
    
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="books.xlsx"'
    return response
