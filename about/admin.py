from django.contrib import admin
from . models import AboutPage


class ProductAdmin(admin.ModelAdmin):
    """Renders stored content to the Django admin panel"""
    list_display = (
        'content',
        'last_updated',
        'author',
    )

    ordering = ('last_updated',)


admin.site.register(AboutPage, ProductAdmin)
