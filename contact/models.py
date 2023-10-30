from django.db import models
from django.shortcuts import reverse


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Requests'

    SUBJECTS = (
        ('1', 'Courses for schools/education'),
        ('2', 'Pricing Inquiry'),
        ('3', 'Business Inquiry'),
        ('4', 'Trouble using the site'),
        ('5', "Trouble accessing my course"),
        ('6', "Recover my account"),
        ('7', "Other"),
    )

    name = models.CharField(max_length=254)
    email = models.EmailField()
    subject = models.CharField(choices=SUBJECTS, max_length=254,)
    message = models.TextField(max_length=1024)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('contact_success')