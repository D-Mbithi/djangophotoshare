# Generated by Django 4.1 on 2022-08-25 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0004_alter_comment_options_photo_likes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="user", new_name="author",
        ),
    ]
