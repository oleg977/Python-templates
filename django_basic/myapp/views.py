from django.shortcuts import render

def index(request):
    """Главная страница."""
    return render(request, 'index.html')

def about(request):
    """Страница 'О нас'."""
    return render(request, 'about.html')