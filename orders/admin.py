from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # find out what list_display does
    list_display = ['size', 'order_status', 'quantity', 'created_at']
#     find out what list_filter does
    list_filter = ['created_at', 'order_status', 'size']
