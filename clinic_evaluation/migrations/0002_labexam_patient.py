# Generated by Django 3.2.7 on 2021-10-26 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('clinic_evaluation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labexam',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
