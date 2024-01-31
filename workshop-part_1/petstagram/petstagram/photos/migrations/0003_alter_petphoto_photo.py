# Generated by Django 4.2.9 on 2024-01-24 19:26

from django.db import migrations, models
import petstagram.photos.models


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0002_petphoto_created_at_petphoto_modified_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="petphoto",
            name="photo",
            field=models.ImageField(
                upload_to="pet_photos/",
                validators=[
                    petstagram.photos.models.MaxFileSizeValidator(limit_value=5242880)
                ],
            ),
        ),
    ]