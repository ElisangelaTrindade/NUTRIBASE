# Generated by Django 3.2.7 on 2021-10-27 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('antopometric_evaluation', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='antopometricevaluation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
