# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('carspace', models.IntegerField()),
                ('date_available', models.DateField()),
                ('furnished', models.BooleanField()),
                ('suburb', models.TextField()),
                ('bond', models.IntegerField()),
                ('description', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_property', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RentProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('carspace', models.IntegerField()),
                ('date_available', models.DateField()),
                ('furnished', models.BooleanField()),
                ('suburb', models.TextField()),
                ('bond', models.IntegerField()),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('property_image1', models.ImageField(upload_to='rentproperties')),
                ('property_image2', models.ImageField(blank=True, upload_to='rentproperties')),
                ('property_image3', models.ImageField(blank=True, upload_to='rentproperties')),
                ('property_image4', models.ImageField(blank=True, upload_to='rentproperties')),
                ('property_image5', models.ImageField(blank=True, upload_to='rentproperties')),
                ('property_image6', models.ImageField(blank=True, upload_to='rentproperties')),
                ('property_image7', models.ImageField(blank=True, upload_to='rentproperties')),
                ('property_image8', models.ImageField(blank=True, upload_to='rentproperties')),
                ('property_image9', models.ImageField(blank=True, upload_to='rentproperties')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.PropertyType')),
            ],
        ),
        migrations.AddField(
            model_name='buyproperty',
            name='property_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.PropertyType'),
        ),
    ]
