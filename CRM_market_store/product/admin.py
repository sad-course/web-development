from django.contrib import admin
from product.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','name','price', 'quantity','created_at']
    search_fields = ['name','code']
    ordering = ['-created_at']
    list_filter = ['created_at']


admin.site.register(Product, ProductAdmin)