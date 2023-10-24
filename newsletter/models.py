from django.db import models


class Email(models.Model):
    class Meta:
        verbose_name_plural = 'Email Addresses'

    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
