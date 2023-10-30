from django.shortcuts import render
from .models import Contact

from django.views.generic import CreateView


def contact(request):
    return render(request, 'contact/contact_form.html')