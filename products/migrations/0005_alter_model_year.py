# Generated by Django 3.2 on 2023-01-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_friendly_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='year',
            field=models.IntegerField(),
        ),
    ]
