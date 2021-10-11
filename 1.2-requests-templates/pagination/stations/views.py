from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings

import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        bas_book = []
        for row in reader:
            bas_book.append(row)
            
    page = int(request.GET.get('page', 1))
    pagi = Paginator(bas_book, 10)

    if page < 1:
        page = 1
    if page > pagi.num_pages:
        page = pagi.num_pages

    context = {
        'bus_stations': pagi.page(page).object_list,
        'page': pagi.page(page),
    }

    return render(request, 'stations/index.html', context)
