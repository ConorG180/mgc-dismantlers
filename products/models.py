from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class Make(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Model(models.Model):
    make = models.ForeignKey('Make', on_delete=models.PROTECT)
    car_model = models.CharField(max_length=50, null=True, blank=True)
    vehicle_category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.car_model)


class Part(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Categories'


class Color(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Product(models.Model):

    PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

    # Choices to pick side of car that part came from

    SIDE_CHOICES = [
        ('DS', 'Driver side'),
        ('PS', 'Passenger side'),
        ('DSR', 'Driver side rear'),
        ('DSF', 'Driver side front'),
        ('PSR', 'Passenger side rear'),
        ('PSF', 'Passenger side front'),
    ]

    FUEL_CHOICES = [
        ('PETROL', 'Petrol'),
        ('DIESEL', 'Diesel'),
        ('ELECTRIC', 'Electric'),
        ('HYBRID', 'Hybrid'),
    ]

    GRADE_CHOICES = [
        ('A', 'A (Perfect)'),
        ('B', 'B (Great)'),
        ('C', 'C (Good)'),
        ('D', 'D (Fair)'),
    ]

    VEHICLE_CATEGORY_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('HATCHBACK', 'Hatchback'),
        ('SUV', 'SUV'),
        ('COUPE', 'Coupe'),
        ('PICKUP', 'Pickup'),
        ('MINIVAN', 'Van/Minivan'),
        ('CONVERTIBLE', 'Convertible'),
        ('MOTORBIKE', 'Motorbike'),
    ]

    make = models.ForeignKey('Make', on_delete=models.PROTECT)
    car_model = models.ForeignKey('Model', on_delete=models.PROTECT)
    part = models.ForeignKey('Part', on_delete=models.PROTECT)
    model_year = models.ForeignKey('Year', on_delete=models.PROTECT)
    description = models.TextField(max_length=1024, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    grade = models.CharField(max_length=12, choices=GRADE_CHOICES)
    color = models.ForeignKey('Color', on_delete=models.PROTECT)
    fuel = models.CharField(max_length=8, null=True, blank=True, choices=FUEL_CHOICES, default=None)
    side = models.CharField(max_length=21, null=True, blank=True, choices=SIDE_CHOICES, default=None)
    vehicle_category = models.CharField(max_length=21, null=True, blank=True, choices=VEHICLE_CATEGORY_CHOICES)
    on_sale = models.BooleanField(default=False)
    sale_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
    image = models.ImageField(null=True, blank=True, max_length=1024)
    in_a_cart = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.part}"
    
    def create_card_title(self):
        return f"{self.make.name} {self.car_model.car_model} {self.model_year.year} {self.part.name}"

