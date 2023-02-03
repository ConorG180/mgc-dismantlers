# Generated by Django 3.2 on 2023-02-03 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20230203_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='make',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.make'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='car_model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.model'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.color'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='make',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.make'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='model_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.year'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='part',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.part'),
            preserve_default=False,
        ),
    ]
