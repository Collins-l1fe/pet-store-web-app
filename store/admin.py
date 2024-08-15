from django.contrib import admin

from . import models

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    autocomplete_fields = []
    list_display = ['id', 'title']
    list_per_page = 20
    list_filter = ['title']
    list_editable = ['title']
    search_fields = ['title__istartswith']


@admin.register(models.product)
class ProductsAdmin(admin.ModelAdmin):
    autocomplete_fields = []
    list_display = ['id', 'name', 'price', 'inventory']
    list_per_page = 20
    list_filter = ['last_update']
    list_editable = ['price', 'inventory']
    search_fields = ['name__istartswith']

