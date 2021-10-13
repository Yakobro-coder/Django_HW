from django.shortcuts import render, redirect

from phones.models import Phone
from django.conf import settings


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort')
    phones = Phone.objects.all()

    if sort == 'name':
        if settings.NAME_SORT:
            phones = Phone.objects.order_by('-name')
            settings.NAME_SORT = False
        else:
            phones = Phone.objects.order_by('name')
            settings.NAME_SORT = True

    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug__exact=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
