from django.shortcuts import render
from .models import Product

# Create your views here.


def courses(request):

    products = Product.objects.all()

    context = {
        'products': products
    }
    
    return render(request, 'products/courses.html', context)