from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ shows all products, searches and sorts products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)