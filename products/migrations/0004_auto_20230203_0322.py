# Generated by Django 3.2 on 2023-02-03 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fuel',
            field=models.CharField(blank=True, choices=[('PETROL', 'Petrol'), ('DIESEL', 'Diesel'), ('ELECTRIC', 'Electric'), ('HYBRID', 'Hybrid')], default=None, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='grade',
            field=models.CharField(choices=[('A', 'A (Perfect)'), ('B', 'B (Great)'), ('C', 'C (Good)'), ('D', 'D (Fair)')], max_length=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='side',
            field=models.CharField(blank=True, choices=[('DS', 'Driver side'), ('PS', 'Passenger side'), ('DSR', 'Driver side rear'), ('DSF', 'Driver side front'), ('PSR', 'Passenger side rear'), ('PSF', 'Passenger side front')], default=None, max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vehicle_category',
            field=models.CharField(blank=True, choices=[('SEDAN', 'Sedan'), ('HATCHBACK', 'Hatchback'), ('SUV', 'SUV'), ('COUPE', 'Coupe'), ('PICKUP', 'Pickup'), ('MINIVAN', 'Van/Minivan'), ('CONVERTIBLE', 'Convertible'), ('MOTORBIKE', 'Motorbike')], max_length=21, null=True),
        ),
    ]