from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from products.models import Product


def view_basket(request):

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url', reverse('view_basket'))
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        messages.error(request, f'{product.name} is already in your basket!')
    else:
        basket[item_id] = quantity
        messages.success(request, f'{product.name} was added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop[item_id]

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):

    try:
        basket = request.session.get('basket', {})

        basket.pop(item_id)

        request.session['basket'] = basket
        return redirect(reverse('view_basket'))
    except Exception as e:
        messages.error(request, "Oops, that didn't work, please try again.")
        return redirect(reverse('home'))
