# Generated by Django 4.2.2 on 2023-06-22 06:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
