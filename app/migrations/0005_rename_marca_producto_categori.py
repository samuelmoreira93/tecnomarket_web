# Generated by Django 4.2.6 on 2023-10-23 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='marca',
            new_name='categori',
        ),
    ]
