from django.contrib import admin
from . models import Wishlist


class ProductAdmin(admin.ModelAdmin):
    """Displays wishlist items in Django Admin panel"""
    list_display = (
        'user',
        'product',
    )

    ordering = ('product',)


admin.site.register(Wishlist, ProductAdmin)
