# Generated by Django 3.2.7 on 2021-12-02 14:03

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('cpf', cpf_field.models.CPFField(max_length=14, unique=True, verbose_name='CPF')),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('email', models.CharField(db_column='email_patient', max_length=150, verbose_name='email')),
                ('street', models.CharField(db_column='street', max_length=50, verbose_name='street')),
                ('zip_code', models.CharField(db_column='zip_code', default='', max_length=15, verbose_name='zip code')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='gender')),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='location.city', verbose_name='city')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
                'db_table': 'patient',
            },
        ),
    ]
