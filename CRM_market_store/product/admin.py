from django.contrib import admin
from product.models import Category, Product, Supplier
# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'cep']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','name','price', 'quantity','created_at']
    search_fields = ['name','code']
    ordering = ['-created_at']
    list_filter = ['created_at']

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)