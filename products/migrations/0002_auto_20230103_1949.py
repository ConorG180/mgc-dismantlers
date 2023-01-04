# Generated by Django 3.2 on 2023-01-03 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
        migrations.AddField(
            model_name='product',
            name='car_model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.model'),
        ),
    ]