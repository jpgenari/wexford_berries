from django.contrib import admin
from . models import Contact

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
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
