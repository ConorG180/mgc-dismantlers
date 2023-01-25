from django.db import models

# Create your models here.
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

# from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile

# Add in select menu for countries later
class Order(models.Model):
    """
    An order model to hold and track user's orders
    """
    order_number = models.CharField(primary_key=True, max_length=32, null=False, blank=False, unique=True, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town = models.CharField(max_length=40)
    city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=60)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    original_bag = models.TextField(default='')
    stripe_pid = models.CharField(max_length=254, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        # Calculate total of products and set the order_total field
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0

        # if order total > free delivery threshold, free delivery. Else apply standard delivery cost
        if self.order_total >= settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = 0
        else:
            self.delivery_cost = settings.STANDARD_DELIVERY_COST
        
        self.grand_total = self.order_total + self.delivery_cost
        
        # Save the order instance
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set order number.
        Uses internal method of model.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# DO_NOTHING set on product so that, once product is deleted,
# the user can still view the product that they bought from their
# order history. Maybe change this later. Can cause integrity issues.
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        """
        Override original save method and set lineitem total
        and order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return f'part: {self.product.model.make.name} {self.product.model.car_model} {self.product.model.year} {self.product.part.name}  on order {self.order.order_number}'