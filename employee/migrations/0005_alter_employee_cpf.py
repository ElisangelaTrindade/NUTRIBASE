# Generated by Django 3.2.7 on 2021-11-07 01:49

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, unique=True, verbose_name='CPF'),
        ),
    ]
