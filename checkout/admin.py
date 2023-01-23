from django.contrib import admin
from django.apps import apps
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdmin,)
    readonly_fields = ('order_number', 'order_date',
                        'delivery_cost', 'order_total',
                        'grand_total', 'original_bag',
                        'stripe_pid',)

    list_display = [field.name for field in Order._meta.get_fields()]


admin.site.register(Order, OrderAdmin)