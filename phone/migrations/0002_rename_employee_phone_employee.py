# Generated by Django 3.2.7 on 2021-10-27 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='Employee',
            new_name='employee',
        ),
    ]
