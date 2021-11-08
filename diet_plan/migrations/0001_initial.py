# Generated by Django 3.2.7 on 2021-11-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(db_column='description', verbose_name='description')),
                ('date_of_creation', models.DateField(verbose_name='date_of_creation')),
            ],
            options={
                'verbose_name': 'Diet Plan',
                'verbose_name_plural': 'Diet Plans',
                'db_table': 'diet_plan',
            },
        ),
    ]
