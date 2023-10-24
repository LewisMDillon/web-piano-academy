from django.shortcuts import render

from django.views.generic import CreateView

from .models import Email

# Create your views here.


class MailingListCreateView(CreateView):
    model = Email
    fields = ['email']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
