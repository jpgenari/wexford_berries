from django.contrib import admin
from . models import Wishlist

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
    )

    ordering = ('product',)

admin.site.register(Wishlist, ProductAdmin)
