# Generated by Django 3.2.7 on 2021-12-02 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nails', models.CharField(db_column='nails', max_length=100, verbose_name='nails')),
                ('skin', models.CharField(db_column='skin', max_length=100, verbose_name='skin')),
                ('bladder_habits', models.CharField(db_column='bladder_habits', max_length=100, verbose_name='bladder_habits')),
                ('bowel_habits', models.CharField(db_column='bowel_habits', max_length=100, verbose_name='bowel_habits')),
                ('additional_information', models.TextField(blank=True, db_column='additional_information', verbose_name='additional_information')),
                ('date_of_consultation', models.DateField(verbose_name='date_of_consultation')),
                ('updated', models.DateField(verbose_name='updated')),
            ],
            options={
                'verbose_name': 'Clinic Evaluation',
                'verbose_name_plural': 'Clinic Evaluations',
                'db_table': 'clinic_evaluation',
            },
        ),
        migrations.CreateModel(
            name='LabExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_exam', models.CharField(db_column='description', max_length=100, verbose_name='description')),
                ('date_of_exam', models.DateField(verbose_name='date_of_exam')),
                ('upload', models.FileField(db_column='upload', upload_to='', verbose_name='upload')),
                ('exam_information', models.TextField(db_column='name_exam ', verbose_name='name_exam')),
                ('clinic_evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_evaluation.clinicevaluation')),
            ],
            options={
                'verbose_name': 'Laboratorial Exam',
                'verbose_name_plural': 'Laboratorial Exams',
                'db_table': 'lab_exam',
            },
        ),
        migrations.CreateModel(
            name='GastrointestinalTractSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dysphagia', models.BooleanField(db_column='dysphagia', verbose_name='dysphagia')),
                ('pain', models.BooleanField(db_column='pain', verbose_name='pain')),
                ('reflux', models.BooleanField(db_column='reflux', verbose_name='reflux')),
                ('heart_burn', models.BooleanField(db_column='heart_burn', verbose_name='heart_burn')),
                ('constipation', models.BooleanField(db_column='constipation', verbose_name='constipation')),
                ('nausea', models.BooleanField(db_column='nausea', verbose_name='nausea')),
                ('diarrhea', models.BooleanField(db_column='diarrhea', verbose_name='diarrhea')),
                ('others', models.TextField(blank=True, db_column='description', verbose_name='description')),
                ('clinic_evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_evaluation.clinicevaluation', verbose_name='clinic_evaluation')),
            ],
            options={
                'verbose_name': 'Gastrointestinal Tract Symptom',
                'verbose_name_plural': 'Gastrointestinal Tract Symptoms',
                'db_table': 'gastrointestinalt_tract_symptoms',
            },
        ),
    ]
