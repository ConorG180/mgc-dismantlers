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
        ('Driver side', 'DS'),
        ('Passenger side', 'PS'),
        ('Driver side rear', 'DSR'),
        ('Driver side front', 'DSF'),
        ('Passenger side rear', 'PSR'),
        ('Passenger side front', 'PSF'),
    ]

    FUEL_CHOICES = [
        ('Petrol', 'PETROL'),
        ('Diesel', 'DIESEL'),
        ('Electric', 'ELECTRIC'),
        ('Hybrid', 'HYBRID'),
    ]

    GRADE_CHOICES = [
        ('A (Perfect)', 'A'),
        ('B (Great)', 'B'),
        ('C (Good)', 'C'),
        ('D (Fair)', 'D'),
    ]

    VEHICLE_CATEGORY_CHOICES = [
        ('Sedan', 'SEDAN'),
        ('Hatchback', 'HATCHBACK'),
        ('SUV', 'SUV'),
        ('Coupe', 'COUPE'),
        ('Pickup', 'PICKUP'),
        ('Van/Minivan', 'VAN/MINIVAN'),
        ('Convertible', 'CONVERTIBLE'),
        ('Motorbike', 'MOTORBIKE'),
    ]

    make = models.ForeignKey('Make', on_delete=models.PROTECT)
    car_model = models.ForeignKey('Model', on_delete=models.PROTECT)
    part = models.ForeignKey('Part', on_delete=models.PROTECT)
    model_year = models.ForeignKey('Year', on_delete=models.PROTECT)
    description = models.TextField(max_length=254, null=True, blank=True)
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
        return f"{self.car_model.make} {self.car_model} {self.car_model.model_year} {self.part}"
