# Generated by Django 3.2.7 on 2021-10-25 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(db_column='group', max_length=150)),
                ('calories', models.PositiveIntegerField(db_column='calories', default=0)),
            ],
            options={
                'db_table': 'food_group',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(db_column='food_name', max_length=50)),
                ('proteins', models.DecimalField(db_column='protein', decimal_places=1, max_digits=6)),
                ('lipids', models.DecimalField(db_column='lipids', decimal_places=1, max_digits=6)),
                ('cholesterol', models.DecimalField(db_column='cholesterol', decimal_places=1, max_digits=6)),
                ('carbohydrates', models.DecimalField(db_column='carbohydrates', decimal_places=1, max_digits=6)),
                ('dietary_fiber', models.DecimalField(db_column='dietary_fiber', decimal_places=1, max_digits=6)),
                ('iron', models.DecimalField(db_column='iron', decimal_places=1, max_digits=6)),
                ('vitamin_c', models.DecimalField(db_column='vitamin_C', decimal_places=1, max_digits=6)),
                ('calcium', models.DecimalField(db_column='calcium', decimal_places=1, max_digits=6)),
                ('calories', models.DecimalField(db_column='calories', decimal_places=1, max_digits=6)),
                ('weight', models.DecimalField(db_column='weight', decimal_places=1, max_digits=6)),
                ('food_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_group.foodgroup')),
            ],
            options={
                'db_table': 'food',
            },
        ),
    ]
