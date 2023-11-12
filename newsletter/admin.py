from django.contrib import admin
from .models import Email


class EmailAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'id',
    )


admin.site.register(Email, EmailAdmin)
