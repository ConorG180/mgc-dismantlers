from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Make(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Model(models.Model):
    make = models.ForeignKey('Make', on_delete=models.PROTECT)
    car_model = models.CharField(max_length=50, null=True, blank=True)
    year = model.DateField()
    vehicle_category = models.CharField(max_length=50)

    def __str__(self):
        return self.car_model


class Part(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name