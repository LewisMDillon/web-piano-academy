from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product

# Create your views here.


def courses(request):

    products = Product.objects.all()

    context = {
        'products': products
    }
    
    return render(request, 'products/courses.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    
    return render(request, 'products/product_detail.html', context)