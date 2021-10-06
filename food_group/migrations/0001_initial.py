# Generated by Django 3.2.7 on 2021-10-06 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diet_plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(db_column='group', max_length=150)),
                ('weight', models.DecimalField(db_column='weight', decimal_places=1, max_digits=8)),
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
                ('weigh', models.DecimalField(db_column='weight', decimal_places=1, max_digits=8)),
                ('diet_plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='diet_plan.dietplan')),
                ('food_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_group.foodgroup')),
            ],
            options={
                'db_table': 'food',
            },
        ),
    ]
