# Generated by Django 3.2 on 2023-01-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_a_cart',
            field=models.BooleanField(default=False),
        ),
    ]