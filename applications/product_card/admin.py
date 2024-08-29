from django.contrib import admin
from .models import ProductCard, ProductCardImage

class ProductImageInline(admin.TabularInline):
    model = ProductCardImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(ProductCard, ProductAdmin)
