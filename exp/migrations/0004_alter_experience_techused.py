# Generated by Django 5.0.6 on 2024-05-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exp", "0003_alter_experience_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="techUsed",
            field=models.ManyToManyField(blank=True, to="exp.tech"),
        ),
    ]