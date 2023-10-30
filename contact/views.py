from django.shortcuts import render
from .models import Contact
from django.contrib import messages


from django.views.generic import CreateView


class ContactFormCreateView(CreateView):
    model = Contact
    fields = [
        'email',
        'name',
        'subject',
        'message'
        ]

    def get_initial(self):
        if self.request.user.is_authenticated:
            # Get the initial dictionary from the superclass method
            initial = super(ContactFormCreateView, self).get_initial()
            initial = initial.copy()
            initial['email'] = self.request.user.email
            return initial

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.info(
            self.request,
            "Message Sent!"
            )
        return super().form_valid(form)


def ContactSuccess(request):
    return render(request, 'contact/contact_success.html')
