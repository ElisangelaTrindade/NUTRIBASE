# Generated by Django 3.2.7 on 2021-10-25 02:04

import cpffield.cpffield
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('health_history', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', cpffield.cpffield.CPFField(max_length=14, unique=True, verbose_name='CPF')),
                ('birthday', models.DateField()),
                ('email', models.CharField(db_column='email_patient', max_length=150)),
                ('street', models.CharField(db_column='street', max_length=50)),
                ('zip_code', models.CharField(db_column='zip_code', default='', max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='location.city')),
                ('family_health_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_history.familyhealthhistory')),
                ('patient_health_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_history.patienthealthhistory')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]
