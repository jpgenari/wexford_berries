from django.contrib import admin
from . models import Product


class ProductAdmin(admin.ModelAdmin):
    """Renders products in the database on Django admin panel"""
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

admin.site.register(Product, ProductAdmin)
