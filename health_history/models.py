from django.db import models

# Create your models here.

class FamilyHealthHistory(models.Model):
  obesity = models.BooleanField(db_column='obesity')
  cardiovascular_disease = models.BooleanField( db_column='cardiovascular_disease')
  hypertension = models.BooleanField (db_column='hypertension')
  cancer = models.BooleanField (db_column='cancer')
  diabetes = models.BooleanField (db_column='diabetes')
  dyslipidemia = models.BooleanField(db_column='dyslipidemia')
  others = models.TextField( db_column='others')
  class Meta:
    db_table ='family_health_history' 

class PatientHealthHistory(models.Model):
  obesity = models.BooleanField(db_column='obesity')
  cardiovascular_disease = models.BooleanField( db_column='cardiovascular_disease')
  hypertension = models.BooleanField(db_column='hypertension')
  cancer = models.BooleanField(db_column='cancer')
  diabetes = models.BooleanField( db_column='diabetes')
  dyslipidemia = models.BooleanField(db_column='dyslipidemia')
  others = models.TextField (db_column='others')

  class Meta:
    db_table ='patient_health_history' 