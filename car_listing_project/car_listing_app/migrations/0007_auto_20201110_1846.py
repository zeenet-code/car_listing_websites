# Generated by Django 3.1.1 on 2020-11-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_listing_app', '0006_auto_20201110_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_product',
            name='car_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
