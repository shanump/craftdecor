from django.contrib import admin

from .models import Categories, Products

class CategoriesAdmin(admin.ModelAdmin):
    thumbnail = ('thumbnail')  # List of fields to make read-only

class ProductsAdmin(admin.ModelAdmin):
    thumbnail = ('thumbnail')  # List of fields to make read-only


admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Products,ProductsAdmin)

