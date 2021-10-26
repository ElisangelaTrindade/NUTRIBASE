# Generated by Django 3.2.7 on 2021-10-26 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0001_initial'),
        ('clinic_evaluation', '0002_labexam_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='labexam',
            name='register_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gastrointestinaltractsymptoms',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='gastrointestinaltractsymptoms',
            name='registered_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clinicevaluation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='clinicevaluation',
            name='registered_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
