from django.contrib import admin
from django.apps import apps
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    fields = ('order', 'product', 'quantity', 'lineitem_total')


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = (OrderLineItemAdmin,)
    readonly_fields = (
        'order_number', 'order_date',
        'delivery_cost', 'order_total',
        'grand_total', 'original_bag',
        'stripe_pid',
    )
    ordering = ('grand_total',)


admin.site.register(Order, OrderAdmin)
