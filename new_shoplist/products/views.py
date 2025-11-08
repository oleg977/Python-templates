from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

def product_list(request):
    # Поиск по названию
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    # Пагинация
    paginator = Paginator(products, 6)  # 6 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'products': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })