# Generated by Django 4.2.6 on 2023-11-03 18:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job",
            old_name="image",
            new_name="imagefun",
        ),
    ]
