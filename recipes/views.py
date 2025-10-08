from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })


def search(request):
    term = request.GET.get('q', '').strip()
    results = []
    if term:
        # gerar resultados fictícios com base no termo
        results = [make_recipe() for _ in range(6)]

    return render(request, 'recipes/pages/home.html', context={
        'recipes': results,
        'search_term': term,
    })