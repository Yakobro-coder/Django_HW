from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'салат': {
        'картофель, гр.': 100,
        'морковь, гр.': 50,
        'огурцы, гр.':50,
        'горошек, гр.': 30,
        'майонез, мл.': 70,
    },
    'пицца': {
        'сыр, гр.': 50,
        'томаты,гр.': 50,
        'тесто, гр.': 100,
        'бекон, гр.': 30,
        'колбаса, гр.': 30,
        'грибы, гр.': 20,
    },
    'фруктовый десерт': {
        'хурма, гр.': 60,
        'киви,гр.': 60,
        'творог, гр.': 60,
        'сахар, гр.': 10,
        'мед, мл.': 50,
    }
}


def home_view(request):
    template_name = 'calculator/home.html'
    recipe_list = [bludo for bludo in DATA]
    context = {
        'recipes': recipe_list
    }
    return render(request, template_name, context)


def recipes_view(request, recipe):
    template_name = 'calculator/index.html'
    servings = request.GET.get('servings', None)

    if servings is not None:
        servings = int(servings)
        serv_bludo = {ingrid: value*servings for ingrid, value in DATA.get(recipe).items()}
        print(serv_bludo)
        context = {
            'recipe': serv_bludo
        }
    else:
        context = {
            'recipe': DATA.get(recipe)
        }
    return render(request, template_name, context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
