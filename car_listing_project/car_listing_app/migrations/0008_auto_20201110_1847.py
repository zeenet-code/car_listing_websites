# Generated by Django 3.1.1 on 2020-11-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_listing_app', '0007_auto_20201110_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_product',
            name='car_speed',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
