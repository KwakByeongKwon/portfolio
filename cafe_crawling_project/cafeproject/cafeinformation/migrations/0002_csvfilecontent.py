# Generated by Django 4.2.7 on 2023-11-30 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cafeinformation", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CsvFilecontent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file_data", models.TextField()),
                (
                    "csvfile_reference",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cafeinformation.csvfile",
                    ),
                ),
            ],
        ),
    ]
