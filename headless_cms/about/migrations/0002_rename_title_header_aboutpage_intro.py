# Generated by Django 4.2.11 on 2024-04-08 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpage',
            old_name='title_header',
            new_name='intro',
        ),
    ]
