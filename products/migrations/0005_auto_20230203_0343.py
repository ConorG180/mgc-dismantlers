# Generated by Django 3.2 on 2023-02-03 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230203_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.model'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.make'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.year'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.part'),
        ),
    ]
