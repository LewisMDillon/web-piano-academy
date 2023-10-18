from django.shortcuts import render


def view_basket(request):

    return render(request, 'basket/basket.html')