# Generated by Django 3.2.7 on 2021-10-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nails', models.CharField(db_column='nails', max_length=100)),
                ('skin', models.CharField(db_column='skin', max_length=100)),
                ('bladder_habits', models.CharField(db_column='bladder_habits', max_length=100)),
                ('bowel_habits', models.CharField(db_column='bowel_habits', max_length=100)),
                ('additional_information', models.TextField(db_column='additional_information')),
                ('date_of_consultation', models.DateField()),
                ('updated', models.DateField()),
            ],
            options={
                'db_table': 'clinic_evaluation',
            },
        ),
        migrations.CreateModel(
            name='GastrointestinalTractSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dysphagia', models.BooleanField(db_column='dysphagia')),
                ('pain', models.BooleanField(db_column='pain')),
                ('reflux', models.BooleanField(db_column='reflux')),
                ('heart_burn', models.BooleanField(db_column='heart_burn')),
                ('constipation', models.BooleanField(db_column='constipation')),
                ('nausea', models.BooleanField(db_column='nausea')),
                ('diarrhea', models.BooleanField(db_column='diarrhea')),
                ('others', models.TextField(db_column='description')),
            ],
            options={
                'db_table': 'gastrointestinalt_tract_symptoms',
            },
        ),
        migrations.CreateModel(
            name='LabExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_exam', models.CharField(db_column='description', max_length=100)),
                ('date_of_exam', models.DateField()),
                ('upload', models.FileField(db_column='upload', upload_to='')),
                ('exam_information', models.TextField(db_column='name_exam ')),
            ],
            options={
                'db_table': 'lab_exam',
            },
        ),
    ]
