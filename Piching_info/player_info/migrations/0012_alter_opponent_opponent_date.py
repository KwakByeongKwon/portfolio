# Generated by Django 4.2.7 on 2023-12-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("player_info", "0011_alter_opponent_opponent_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opponent",
            name="opponent_date",
            field=models.DateTimeField(default=""),
        ),
    ]