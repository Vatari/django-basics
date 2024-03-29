# Generated by Django 4.2.9 on 2024-02-24 11:43

import django.core.validators
from django.db import migrations, models
import world_of_speed.cars.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rally', 'Rally'), ('Open-wheel', 'Open-wheel'), ('Kart', 'Kart'), ('Drag', 'Drag'), ('Other', 'Other')], max_length=10, verbose_name='Type')),
                ('model', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Model')),
                ('year', models.IntegerField(validators=[world_of_speed.cars.models.validate_year], verbose_name='Year')),
                ('image_url', models.URLField(default='https://...', error_messages={'This image URL is already in use! Provide a new one.'}, unique=True, verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)], verbose_name='Price')),
            ],
        ),
    ]
