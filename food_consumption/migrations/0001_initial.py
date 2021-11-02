# Generated by Django 3.2.7 on 2021-11-01 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_drink', models.BooleanField(db_column='soft_drink')),
                ('candy', models.BooleanField(db_column='candy')),
                ('deep_fried', models.BooleanField(db_column='deep_fried')),
                ('fast_food', models.BooleanField(db_column='fast_food')),
                ('processed_food', models.BooleanField(db_column='processed_food')),
                ('canned_food', models.BooleanField(db_column='canned')),
                ('fruits', models.BooleanField(db_column='fruits')),
                ('vegetables', models.BooleanField(db_column='vegetables')),
                ('others', models.TextField(db_column='description')),
            ],
            options={
                'db_table': 'food_consumption',
            },
        ),
        migrations.CreateModel(
            name='FoodIntolerance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intolerance_description', models.TextField(db_column='intolerance_description')),
            ],
            options={
                'db_table': 'food_intolerance',
            },
        ),
        migrations.CreateModel(
            name='FoodPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(db_column='description')),
                ('food_consumption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_consumption.foodconsumption')),
            ],
            options={
                'db_table': 'food_preferences',
            },
        ),
    ]
