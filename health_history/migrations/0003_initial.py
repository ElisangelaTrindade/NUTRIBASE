# Generated by Django 3.2.7 on 2021-12-02 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('health_history', '0002_patienthealthhistory_patient'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthealthhistory',
            name='registered_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='registered_by'),
        ),
        migrations.AddField(
            model_name='familyhealthhistory',
            name='patient_health_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_history.patienthealthhistory', verbose_name='patient_health_history'),
        ),
    ]
