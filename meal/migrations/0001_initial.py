# Generated by Django 3.2.7 on 2021-10-25 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food_diary', '0001_initial'),
        ('diet_plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_meal', models.CharField(db_column='type_meal', max_length=50)),
                ('time_meal', models.DateTimeField(db_column='time_meal')),
                ('diet_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet_plan.dietplan')),
                ('food_diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_diary.fooddiary')),
            ],
            options={
                'db_table': 'meal',
            },
        ),
    ]
