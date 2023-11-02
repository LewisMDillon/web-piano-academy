from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings

from django.views.generic import CreateView, DeleteView

from .models import Email

# Create your views here.


@login_required
def unsubscribe(request):
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


@login_required
def mailing_list_delete(request, email):

    model = Email
    addresses = Email.objects.all()
    try:
        Email.objects.get(email=request.user.email)
    except ObjectDoesNotExist:
        messages.error(
            request,
            "You are not subscribed"
            )
        return redirect(reverse('home'))

    thisEmail = Email.objects.get(email=request.user.email)

    if request.user.email == email:
        email = get_object_or_404(Email, email=email)
        email.delete()
        messages.info(request, 'You have unsubscribed from the mailing list')
        return redirect(reverse('home'))
    else:
        messages.error(
            request,
            "Sorry, that didn't work. Please double check"
            " that you are logged in, then try that again."
            )
        return redirect(reverse('home'))
