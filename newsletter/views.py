from django.shortcuts import render
from django.contrib import messages


from django.views.generic import CreateView

from .models import Email

# Create your views here.


class MailingListCreateView(CreateView):
    model = Email
    fields = ['email']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.info(
            self.request,
            "Thanks for subscribing to our newsletter!"
            " Be on the lookout for exciting news from"
            " Web Piano Academy!"
            )
        return super().form_valid(form)
