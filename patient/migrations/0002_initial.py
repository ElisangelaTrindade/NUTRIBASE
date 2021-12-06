# Generated by Django 3.2.7 on 2021-12-06 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='registered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='registered_by'),
        ),
        migrations.AddField(
            model_name='patient',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.state', verbose_name='state'),
        ),
    ]
