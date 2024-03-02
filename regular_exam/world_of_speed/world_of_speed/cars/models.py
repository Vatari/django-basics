from django.core.exceptions import ValidationError

from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from world_of_speed.profiles.models import Profile


def validate_year(value):
    if not (1999 <= value <= 2030):
        raise ValidationError("Year must be between 1999 and 2030!")


class Car(models.Model):
    TYPE_CHOICES = [
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    ]

    type = models.CharField(
        verbose_name='Type',
        max_length=10,
        choices=TYPE_CHOICES,
    )

    model = models.CharField(
        verbose_name='Model',
        max_length=15,
        validators=[MinLengthValidator(1)],
    )

    year = models.IntegerField(
        verbose_name='Year',
        validators=[validate_year],
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        unique=True,
        error_messages={'unique': 'This image URL is already in use! Provide a new one.'},
        default="https://..."
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=[MinValueValidator(1.0)],
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='cars',
        verbose_name='Owner',
        editable=False,
        null=True  # Allow null values
    )
