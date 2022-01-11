from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Admin, Customer, Cart, CartProduct, Order])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
