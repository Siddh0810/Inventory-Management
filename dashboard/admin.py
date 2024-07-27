from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group

admin.site.site_header = 'Stock Management DashBoard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','category')
    list_filter = ['category']

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)