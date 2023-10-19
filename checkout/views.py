from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "You don't have anything in your basket!")
        return redirect(reverse('courses'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O2unyAYWAqORA4GchES5VgHwTGtpJaG82T5dqrigzzdDh4GVS03fDRqZFB02jq43UyMib5fX2Rtt9BAC0FB71vY00DdUi1Yxg'
        
    }

    return render(request, template, context)