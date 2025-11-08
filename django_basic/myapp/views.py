# myapp/views.py

from django.shortcuts import render

def index(request):
    """Главная страница."""
    context = {
        'title': 'Главная страница шаблона',
        'content': 'Это базовая структура приложения Django.'
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    """Страница "О нас"."""
    context = {
        'title': 'О проекте',
        'content': 'Это страница с описанием проекта.'
    }
    return render(request, 'myapp/about.html', context)