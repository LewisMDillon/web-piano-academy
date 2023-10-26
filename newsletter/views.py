from django.shortcuts import render
from django.contrib import messages


from django.views.generic import CreateView

from .models import Email

# Create your views here.


class MailingListCreateView(CreateView):
    model = Email
    fields = ['email']

    def get_initial(self):
        if self.request.user.is_authenticated:
            # Get the initial dictionary from the superclass method
            initial = super(MailingListCreateView, self).get_initial()
            # Copy the dictionary so we don't accidentally change a mutable dict
            initial = initial.copy()
            initial['email'] = self.request.user.email
            return initial

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.info(
            self.request,
            "Thanks for subscribing to our newsletter!"
            " Be on the lookout for exciting news from"
            " Web Piano Academy!"
            )
        return super().form_valid(form)
