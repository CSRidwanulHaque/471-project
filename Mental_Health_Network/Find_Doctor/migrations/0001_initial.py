# Generated by Django 5.0.1 on 2024-03-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Counselor",
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
                ("name", models.CharField(max_length=200)),
                ("authorized_id", models.CharField(max_length=10, unique=True)),
                ("qualifications", models.TextField()),
                ("total_experience", models.PositiveIntegerField()),
                ("consultation_days", models.CharField(max_length=500)),
                ("consultation_time", models.CharField(max_length=250)),
                (
                    "appointment_fees",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
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
                ("name", models.CharField(max_length=200)),
                ("authorized_id", models.CharField(max_length=10, unique=True)),
                ("qualifications", models.TextField()),
                ("total_experience", models.PositiveIntegerField()),
                ("consultation_days", models.CharField(max_length=500)),
                ("consultation_time", models.CharField(max_length=250)),
                ("off_days", models.CharField(max_length=100)),
                (
                    "appointment_fees",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
    ]
