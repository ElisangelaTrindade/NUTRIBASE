# Generated by Django 3.2.7 on 2021-12-02 14:03

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diet_plan', '0001_initial'),
        ('antopometric_evaluation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionalConduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_nutritional_conduct', models.TextField(blank=True, db_column='description_nutritional_conduct', verbose_name='Nutricional Conduct')),
                ('date_of_consultation', models.DateField(verbose_name='date_of_consultation')),
                ('exercise_type', models.CharField(choices=[('L', 'Light'), ('M', 'Moderate'), ('I', 'Intensive')], max_length=1, verbose_name='exercise')),
                ('antopometric_evaluation', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='patient', chained_model_field='patient', on_delete=django.db.models.deletion.CASCADE, to='antopometric_evaluation.antopometricevaluation', verbose_name='antopomeetric_evaluation')),
                ('diet_plan', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diet_plan.dietplan', verbose_name='diet_plan')),
            ],
            options={
                'verbose_name': 'Nutricional Conduct',
                'verbose_name_plural': 'Nutricional Conducts',
                'db_table': 'nutritional_conduct',
            },
        ),
    ]
