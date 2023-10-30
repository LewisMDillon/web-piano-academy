from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'subject',
    )


admin.site.register(Contact, ContactAdmin)
