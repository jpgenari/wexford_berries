from django.contrib import admin
from . models import Contact


class ProductAdmin(admin.ModelAdmin):
    """Renders all received messaged in the database to Django admin panel"""
    list_display = (
        'name',
        'email',
        'subject',
        'order_number',
        'message',
        'created_on',
    )

    ordering = ('created_on',)


admin.site.register(Contact, ProductAdmin)
