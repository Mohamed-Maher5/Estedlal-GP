# Generated by Django 5.0.4 on 2024-04-21 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_rename_user_email_answer_user_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="answer", options={"ordering": ["question_text"]},
        ),
        migrations.RemoveField(model_name="answer", name="user",),
        migrations.AddField(
            model_name="answer",
            name="login",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="question",
                to="home.login",
            ),
        ),
    ]
