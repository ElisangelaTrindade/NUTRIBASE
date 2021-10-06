# Generated by Django 3.2.7 on 2021-10-06 16:42

import cpffield.cpffield
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire_date', models.DateField(db_column='hire_date')),
                ('cpf', cpffield.cpffield.CPFField(max_length=14, unique=True, verbose_name='CPF')),
                ('birthday', models.DateField()),
                ('email', models.CharField(db_column='email_patient', max_length=150)),
                ('street', models.CharField(db_column='street', max_length=50)),
                ('zip_code', models.CharField(default='', max_length=9)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='location.city')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
