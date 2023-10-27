from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.conf import settings

from django.views.generic import CreateView, DeleteView

from .models import Email

# Create your views here.


def unsub(request):
    return render(request, 'newsletter/unsubscribe.html')


class MailingListCreateView(CreateView):
    model = Email
    email_list = Email.objects.all()
    fields = ['email']

    def get_initial(self):
        if self.request.user.is_authenticated:
            # Get the initial dictionary from the superclass method
            initial = super(MailingListCreateView, self).get_initial()
            initial = initial.copy()
            initial['email'] = self.request.user.email
            return initial

    def _send_confirmation_email(self):
        """Send the user a confirmation email"""
        email = self.request.POST.get('email')
        subject = render_to_string(
            'newsletter/confirmation_emails/confirmation_email_subject.txt',
            )
        body = render_to_string(
            'newsletter/confirmation_emails/confirmation_email_body.txt',
            {'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email]
        )

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.info(
            self.request,
            "Thanks for subscribing to our newsletter!"
            " Be on the lookout for exciting news from"
            " Web Piano Academy!"
            )
        self._send_confirmation_email()
        return super().form_valid(form)


class MailingListDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView
        ):
    model = Email
    success_url = reverse_lazy('home')
    success_message = (
        'You have unsubscribed from the mailing list.'
    )

    def test_func(self):
        email = self.get_object()
        if self.request.user.email == email.email:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(
            MailingListDeleteView, self
            ).delete(request, *args, **kwargs)