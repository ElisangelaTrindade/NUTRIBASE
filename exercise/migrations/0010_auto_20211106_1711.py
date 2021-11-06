# Generated by Django 3.2.7 on 2021-11-06 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercise', '0009_auto_20211106_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='registered_by',
        ),
        migrations.AddField(
            model_name='exercisetype',
            name='registered_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='registered_by'),
            preserve_default=False,
        ),
    ]
