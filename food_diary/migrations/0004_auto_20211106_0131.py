# Generated by Django 3.2.7 on 2021-11-06 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20211106_0131'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_diary', '0003_fooddiary_registered_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fooddiary',
            options={'verbose_name': 'Food Diary', 'verbose_name_plural': 'Food Diaries'},
        ),
        migrations.AlterField(
            model_name='fooddiary',
            name='date_of_consultation',
            field=models.DateField(verbose_name='date_of_consultation'),
        ),
        migrations.AlterField(
            model_name='fooddiary',
            name='description',
            field=models.TextField(db_column='description', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='fooddiary',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient', verbose_name='patient'),
        ),
        migrations.AlterField(
            model_name='fooddiary',
            name='registered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='registered_by'),
        ),
    ]
