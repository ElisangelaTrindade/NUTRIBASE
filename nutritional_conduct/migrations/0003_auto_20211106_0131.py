# Generated by Django 3.2.7 on 2021-11-06 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet_plan', '0004_auto_20211106_0131'),
        ('patient', '0003_auto_20211106_0131'),
        ('food_consumption', '0004_auto_20211106_0131'),
        ('nutritional_conduct', '0002_nutritionalconduct_patient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nutritionalconduct',
            options={'verbose_name': 'Nutricional Conduct', 'verbose_name_plural': 'Nutricional Conducts'},
        ),
        migrations.AlterField(
            model_name='nutritionalconduct',
            name='additional_information',
            field=models.TextField(blank=True, db_column='additional_information', verbose_name='additional_information'),
        ),
        migrations.AlterField(
            model_name='nutritionalconduct',
            name='caloric_needs',
            field=models.DecimalField(db_column='caloric', decimal_places=3, max_digits=8, verbose_name='caloric_needs'),
        ),
        migrations.AlterField(
            model_name='nutritionalconduct',
            name='diet_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet_plan.dietplan', verbose_name='diet_plan'),
        ),
        migrations.AlterField(
            model_name='nutritionalconduct',
            name='food_consumption',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_consumption.foodconsumption', verbose_name='food_consumption'),
        ),
        migrations.AlterField(
            model_name='nutritionalconduct',
            name='food_intolerance',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_consumption.foodintolerance', verbose_name='food_intolerance'),
        ),
        migrations.AlterField(
            model_name='nutritionalconduct',
            name='food_preferences',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_consumption.foodpreferences', verbose_name='food_preferences'),
        ),
        migrations.AlterField(
            model_name='nutritionalconduct',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient', verbose_name='patient'),
        ),
    ]
