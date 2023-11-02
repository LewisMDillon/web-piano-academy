from django.db import models
from django.utils import timezone
import datetime


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    LEVEL_CHOICES = (
        ('1-Beginner', '1-Beginnner'),
        ('2-Intermediate', '2-Intermediate'),
        ('3-Advanced', '3-Advanced')
    )

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    level = models.CharField(
        choices=LEVEL_CHOICES, max_length=254, null=True, blank=True
        )
    level_display_name = models.CharField(
        max_length=254, null=True, blank=True
        )
    name = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)
    course_url = models.URLField(max_length=1024, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
