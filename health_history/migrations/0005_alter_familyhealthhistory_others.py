# Generated by Django 3.2.7 on 2021-11-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_history', '0004_alter_familyhealthhistory_registered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyhealthhistory',
            name='others',
            field=models.TextField(blank=True, db_column='others'),
        ),
    ]
