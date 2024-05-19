from django.contrib import admin
from . models import AboutPage

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'last_updated',
        'author',
    )

    ordering = ('last_updated',)

admin.site.register(AboutPage, ProductAdmin)
