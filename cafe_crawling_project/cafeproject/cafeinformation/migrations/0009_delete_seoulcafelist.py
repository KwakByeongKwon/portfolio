# Generated by Django 4.2.7 on 2023-12-01 01:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cafeinformation", "0008_seoulcafelist"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SeoulCafeList",
        ),
    ]