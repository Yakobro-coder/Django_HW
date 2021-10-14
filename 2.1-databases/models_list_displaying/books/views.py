from django.shortcuts import render
from books.models import Book
from datetime import date


def books_view(request, year=None, mouth=None, day=None):
    page = None
    has_previous = {'has_previous': False}
    has_next = {'has_next': False}

    template = 'books/books_list.html'
    books = Book.objects.all()

    if year is not None and mouth is not None and day is not None:
        pub_date = date(year, mouth, day)
        books = Book.objects.get(pub_date__exact=pub_date)
        template = 'books/books_pages.html'

        if Book.objects.filter(pub_date__lt=pub_date)[:1].count() > 0:
            pres_page = Book.objects.filter(pub_date__lt=pub_date)[:1].get().pub_date
            has_previous = {'has_previous': True}
        else:
            pres_page = date(1700, 12, 1)

        if Book.objects.filter(pub_date__gt=pub_date)[:1].count() > 0:
            next_page = Book.objects.filter(pub_date__gt=pub_date)[:1].get().pub_date
            has_next = {'has_next': True}
        else:
            next_page = date(1700, 12, 1)
        page = {
            'previous_page_number': pres_page.strftime('%Y-%m-%d'),
            'number': pub_date.strftime('%Y-%m-%d'),
            'next_page_number': next_page.strftime('%Y-%m-%d'),
        }

    context = {
        'books': books,
        'page': {**page, **has_previous, **has_next}
    }
    return render(request, template, context)
