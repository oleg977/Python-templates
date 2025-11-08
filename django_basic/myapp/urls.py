# myapp/urls.py

from django.urls import path
from . import views

# ВАЖНО: Неймспейс приложения
app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # Здесь можно добавить path('forms/', views.form_view, name='forms'),
]