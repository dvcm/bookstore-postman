# Generated by Django 4.2 on 2023-04-17 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_slug_category_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='price',
            new_name='slug',
        ),
    ]
