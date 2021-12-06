# Generated by Django 3.2.7 on 2021-12-06 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('food_consumption', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodconsumption',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient', verbose_name='patient'),
        ),
    ]
