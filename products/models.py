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
    year = models.DateField()
    vehicle_category = models.CharField(max_length=50)

    def __str__(self):
        return self.car_model


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


class Product(models.Model):

    PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

    # Choices to pick side of car that part came from
    DRIVER_SIDE = 'DS'
    PASSENGER_SIDE = 'PS'
    DRIVER_SIDE_REAR = 'DSR'
    DRIVER_SIDE_FRONT = 'DSF'
    PASSENGER_SIDE_FRONT = 'PSF'
    PASSENGER_SIDE_REAR = 'PSR'

    SIDE_CHOICES = [
        (DRIVER_SIDE, 'Driver side'),
        (PASSENGER_SIDE, 'Passenger side'),
        (DRIVER_SIDE_REAR, 'Driver side rear'),
        (DRIVER_SIDE_FRONT, 'Driver side front'),
        (PASSENGER_SIDE_REAR, 'Passenger side rear'),
        (PASSENGER_SIDE_FRONT, 'Passenger side front'),
    ]

    # Choices to pick color of the part
    WHITE = 'WHITE'
    BLACK = 'BLACK'
    GRAY = 'GRAY'
    SILVER = 'SILVER'
    BLUE = 'BLUE'
    RED = 'RED'
    BROWN = 'BROWN'
    GREEN = 'GREEN'
    ORANGE = 'ORANGE'
    BEIGE = 'BEIGE'
    PURPLE = 'PURPLE'
    GOLD = 'GOLD'
    YELLOW = 'YELLOW'
    INDIGO = 'INDIGO'
    VIOLET = 'VIOLET'

    COLOR_CHOICES = [
        (WHITE, 'White'),
        (BLACK, 'Black'),
        (GRAY, 'Gray'),
        (SILVER, 'Silver'),
        (BLUE, 'Blue'),
        (RED, 'red'),
        (BROWN, 'Brown'),
        (GREEN, 'Green'),
        (ORANGE, 'Orange'),
        (BEIGE, 'Beige'),
        (PURPLE, 'Purple'),
        (GOLD, 'Gold'),
        (YELLOW, 'Yellow'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
    ]

    # Choices to pick fuel of car that part came from
    PETROL = 'PETROL'
    DIESEL = 'DIESEL'
    ELECTRIC = 'ELECTRIC'
    HYBRID = 'HYBRID'

    FUEL_CHOICES = [
        (PETROL, 'Petrol'),
        (DIESEL, 'Diesel'),
        (ELECTRIC, 'Electric'),
        (HYBRID, 'Hybrid'),
    ]

    # Choices to pick Grade of the part
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'

    GRADE_CHOICES = [
        (A, 'A (Perfect)'),
        (B, 'B (Great)'),
        (C, 'C (Good)'),
        (D, 'D (Fair)'),
    ]

    car_model = models.ForeignKey('Model', on_delete=models.PROTECT, default=1)
    part = models.ForeignKey('Part', on_delete=models.PROTECT)
    description = models.TextField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    color = models.CharField(max_length=6, null=True, blank=True, choices=COLOR_CHOICES, default=None)
    fuel = models.CharField(max_length=8, null=True, blank=True, choices=FUEL_CHOICES, default=None)
    side = models.CharField(max_length=3, null=True, blank=True, choices=SIDE_CHOICES, default=None)
    on_sale = models.BooleanField(default=False)
    sale_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.part}"
