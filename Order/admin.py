from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'paid_amount', 'status', 'transaction_id']
    list_filter = ['status']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'Food', 'price', 'quantity']
    list_filter = ['user']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
