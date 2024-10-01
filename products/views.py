from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ shows all products, including searching and sorting """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)