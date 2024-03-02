import re

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_username(value):
    if len(value) < 3:
        raise ValidationError("Username must be at least 3 chars long!")
    if not all(ch.isalnum() or ch == '_' for ch in value):
        raise ValidationError("Username must contain only letters, digits, and underscores!")


class Profile(models.Model):
    username = models.CharField(
        verbose_name='Username',
        max_length=15,
        unique=True,
        validators=[
            MinLengthValidator(3), validate_username],
    )

    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )

    age = models.IntegerField(
        verbose_name='Age',
        validators=[
            MinValueValidator(21)
        ],
        help_text="Age requirement: 21 years and above.",
    )

    password = models.CharField(
        verbose_name='Password',
        max_length=20
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=25,
        blank=True,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=25,
        blank=True,
    )

    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        blank=True,
    )
