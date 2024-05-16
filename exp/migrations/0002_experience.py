# Generated by Django 5.0.6 on 2024-05-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Experience",
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
                ("company", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=50)),
                ("desc", models.TextField()),
                ("start", models.DateField(default="1998-12-25")),
                ("end", models.DateField(default="1998-12-25")),
                ("techUsed", models.ManyToManyField(to="exp.tech")),
            ],
        ),
    ]