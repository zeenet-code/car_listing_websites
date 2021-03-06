# Generated by Django 3.1.1 on 2020-11-10 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_cate', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_plan_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car_listing_app.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Seller_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=80)),
                ('car_model', models.CharField(max_length=80)),
                ('car_year', models.CharField(max_length=80)),
                ('car_owner', models.CharField(max_length=80)),
                ('car_type', models.CharField(max_length=80)),
                ('car_speed', models.CharField(max_length=80)),
                ('rating', models.IntegerField(default=0)),
                ('car_owner_location', models.CharField(max_length=80)),
                ('car_image', models.ImageField(default='default.jpg', upload_to='product_pics')),
                ('car_price', models.IntegerField(default=0)),
                ('car_description', models.TextField(default='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('area_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_listing_app.area_category')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
