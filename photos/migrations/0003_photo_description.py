# Generated by Django 4.1 on 2022-08-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0002_like_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="description",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
