# Generated by Django 3.2.7 on 2021-12-06 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='registered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_by', to=settings.AUTH_USER_MODEL, verbose_name='registered_by'),
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.state', verbose_name='state'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
