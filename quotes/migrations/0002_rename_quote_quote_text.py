# Generated by Django 5.2 on 2025-04-15 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='quote',
            new_name='text',
        ),
    ]
