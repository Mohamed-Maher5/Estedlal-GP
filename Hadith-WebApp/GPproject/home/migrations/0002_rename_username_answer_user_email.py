# Generated by Django 5.0.4 on 2024-04-21 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answer", old_name="username", new_name="user_email",
        ),
    ]
