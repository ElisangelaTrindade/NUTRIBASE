# Generated by Django 3.2.7 on 2021-11-10 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('antopometric_evaluation', '0004_remove_antopometricevaluation_bmi'),
        ('diet_plan', '0005_remove_dietplan_antopometric_evaluation'),
        ('patient', '0003_alter_patient_cpf'),
        ('nutritional_conduct', '0009_alter_nutritionalconduct_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionalconduct',
            name='diet_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet_plan.dietplan', unique=True, verbose_name='diet_plan'),
        ),
        migrations.AlterUniqueTogether(
            name='nutritionalconduct',
            unique_together={('patient', 'antopometric_evaluation')},
        ),
    ]