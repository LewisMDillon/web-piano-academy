from django.contrib import admin
from .models import Product, Category


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'date_created'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)