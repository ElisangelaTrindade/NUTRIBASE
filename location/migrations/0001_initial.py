# Generated by Django 3.2.7 on 2021-10-27 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='state', max_length=50)),
                ('acrm', models.CharField(db_column='acrm', max_length=3)),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(db_column='city', max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.state')),
            ],
            options={
                'db_table': 'city',
            },
        ),
    ]
