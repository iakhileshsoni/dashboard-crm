from django.contrib import admin
from .models import Customer, Tag, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'date_created']
admin.site.register(Customer, CustomerAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Tag, TagAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'description', 'date_created']
admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'note', 'status', 'date_created']
admin.site.register(Order, OrderAdmin)
