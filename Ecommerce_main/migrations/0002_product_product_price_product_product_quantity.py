# Generated by Django 5.2 on 2025-04-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(null=True),
        ),
    ]
