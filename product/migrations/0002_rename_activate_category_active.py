# Generated by Django 4.1.7 on 2023-03-08 18:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="activate",
            new_name="active",
        ),
    ]
