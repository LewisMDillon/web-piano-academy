from django.db import models
from django.shortcuts import reverse


class Email(models.Model):
    class Meta:
        verbose_name_plural = 'Email Addresses'

    email = models.EmailField(
        max_length=254,
        unique=True,
        error_messages={'unique': "This email is already subscribed."}
        )

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')
