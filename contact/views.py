from django.shortcuts import render, reverse
from .models import Contact
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)


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


class ContactListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
    context_object_name = 'contacts'
    ordering = ['-pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class ContactDetailView(DetailView):
    model = Contact


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ["responded"]
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.info(
            self.request,
            "Successfully Updated!"
            )
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

    def get_success_url(self):
        return reverse('contact-update', kwargs={'pk': self.object.pk})


class ContactDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView
        ):
    model = Contact
    success_url = reverse_lazy('contact_list')
    success_message = (
        'Message Deleted.'
    )

    def test_func(self):
        contact = self.get_object()
        if self.request.user.is_staff:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(
            ContactDeleteView, self
            ).delete(request, *args, **kwargs)

