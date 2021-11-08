# Generated by Django 3.2.7 on 2021-11-08 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food_group', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_meal', models.CharField(db_column='type_meal', max_length=50, verbose_name='type_meal')),
                ('time_meal', models.DateTimeField(db_column='time_meal', verbose_name='time_meal')),
                ('object_id', models.PositiveIntegerField(verbose_name='object_id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='content_type')),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
                'db_table': 'meal',
            },
        ),
        migrations.CreateModel(
            name='MealFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(db_column='weight', decimal_places=1, max_digits=8, verbose_name='weight')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_group.food', verbose_name='food')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.meal', verbose_name='meal')),
            ],
            options={
                'verbose_name': 'Meal Foods',
                'verbose_name_plural': 'Meal Foods',
                'db_table': 'meal_food',
            },
        ),
    ]
