# Generated by Django 3.2.7 on 2021-11-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutritional_conduct', '0003_auto_20211106_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritionalconduct',
            name='date_of_consultation',
            field=models.DateField(default=1, verbose_name='date_of_consultation'),
            preserve_default=False,
        ),
    ]
