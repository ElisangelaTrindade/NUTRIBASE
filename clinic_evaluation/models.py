from django.db import models
from patient.models import Patient
from user.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class ClinicEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name =_('patient'))
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name =_('registered_by'))
  nails= models.CharField(max_length=100, db_column='nails', verbose_name =_('nails'))
  skin = models.CharField(max_length=100, db_column='skin', verbose_name =_('skin'))
  bladder_habits = models.CharField(max_length=100, db_column='bladder_habits', verbose_name =_('bladder_habits'))
  bowel_habits = models.CharField(max_length=100, db_column='bowel_habits', verbose_name =_('bowel_habits')) 
  additional_information= models.TextField(blank=True, db_column='additional_information', verbose_name =_('additional_information')) 
  date_of_consultation=models.DateField(verbose_name =_('date_of_consultation'))
  updated=models.DateField(verbose_name =_('updated'))

  def __str__(self):
    return self.patient.first_name + " " + self.patient.last_name
    
  class Meta:
    db_table ='clinic_evaluation' 
    verbose_name = _('Clinic Evaluation')
    verbose_name_plural = _('Clinic Evaluations')

class GastrointestinalTractSymptoms(models.Model):
  clinic_evaluation = models.ForeignKey(ClinicEvaluation, on_delete=models.CASCADE, verbose_name =_('clinic_evaluation'))
  dysphagia = models.BooleanField (db_column='dysphagia', verbose_name =_('dysphagia'))
  pain = models.BooleanField(db_column='pain' , verbose_name =_('pain'))
  reflux = models.BooleanField( db_column='reflux', verbose_name =_('reflux'))
  heart_burn= models.BooleanField( db_column='heart_burn', verbose_name =_('heart_burn'))
  constipation = models.BooleanField( db_column='constipation', verbose_name =_('constipation')) 
  nausea= models.BooleanField( db_column='nausea', verbose_name =_('nausea'))  
  diarrhea= models.BooleanField( db_column='diarrhea', verbose_name =_('diarrhea')) 
  others = models.TextField(blank=True, db_column='description', verbose_name =_('description'))


  class Meta:
    db_table ='gastrointestinalt_tract_symptoms' 
    verbose_name = _('Gastrointestinal Tract Symptom')
    verbose_name_plural = _('Gastrointestinal Tract Symptoms')

class LabExam (models.Model): 
  clinic_evaluation = models.ForeignKey(ClinicEvaluation, on_delete=models.CASCADE)
  name_exam =models.CharField(max_length=100, db_column='description', verbose_name =_('description'))
  date_of_exam=models.DateField(verbose_name =_('date_of_exam'))
  upload=models.FileField(db_column='upload', verbose_name =_('upload'))
  exam_information = models.TextField(blank=True, db_column='name_exam ', verbose_name =_('name_exam'))

      
  class Meta:
    db_table ='lab_exam' 
    verbose_name = _('Laboratorial Exam')
    verbose_name_plural = _('Laboratorial Exams')