# Generated by Django 4.2.7 on 2023-12-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("player_info", "0005_alter_opponent_opponent_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opponent",
            name="opponent_date",
            field=models.DateTimeField(default=""),
        ),
    ]