# Generated by Django 3.2.7 on 2021-11-10 01:38

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('antopometric_evaluation', '0004_remove_antopometricevaluation_bmi'),
        ('diet_plan', '0003_dietplan_registered_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietplan',
            name='antopometric_evaluation',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='patient', chained_model_field='patient', default=1, on_delete=django.db.models.deletion.CASCADE, to='antopometric_evaluation.antopometricevaluation', verbose_name='antopomeetric_evaluation'),
            preserve_default=False,
        ),
    ]