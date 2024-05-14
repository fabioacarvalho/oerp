from django.contrib import admin
from stock.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_dfilter = ['name',]
    search_fields = ['name',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'qtde', 'unity', 'pn', 'sn', 'component',]
    list_dfilter = ['name', 'category', 'price', 'qtde', 'unity', 'pn', 'sn', 'component',]
    search_fields = ['name', 'category', 'price', 'qtde', 'unity', 'pn', 'sn', 'component',]
