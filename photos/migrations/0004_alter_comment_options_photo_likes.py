# Generated by Django 4.1 on 2022-08-25 19:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("photos", "0003_photo_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment", options={"ordering": ["written_at"]},
        ),
        migrations.AddField(
            model_name="photo",
            name="likes",
            field=models.ManyToManyField(
                related_name="blogpost_like", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
