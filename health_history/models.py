from django.db import models
from patient.models import Patient
from user.models import User


# Create your models here.
class PatientHealthHistory(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  obesity = models.BooleanField(db_column='obesity')
  cardiovascular_disease = models.BooleanField( db_column='cardiovascular_disease')
  hypertension = models.BooleanField(db_column='hypertension')
  cancer = models.BooleanField(db_column='cancer')
  diabetes = models.BooleanField( db_column='diabetes')
  dyslipidemia = models.BooleanField(db_column='dyslipidemia')
  others = models.TextField (blank= True, db_column='others')

  def __str__(self):
    return self.patient.first_name + " " + self.patient.last_name
  
  class Meta:
    db_table ='patient_health_history' 

class FamilyHealthHistory(models.Model):
  patient_health_history= models.ForeignKey(PatientHealthHistory, on_delete=models.CASCADE)
  obesity = models.BooleanField(db_column='obesity')
  cardiovascular_disease = models.BooleanField( db_column='cardiovascular_disease')
  hypertension = models.BooleanField (db_column='hypertension')
  cancer = models.BooleanField (db_column='cancer')
  diabetes = models.BooleanField (db_column='diabetes')
  dyslipidemia = models.BooleanField(db_column='dyslipidemia')
  others = models.TextField(blank=True, db_column='others')
  
  class Meta:
    db_table ='family_health_history' 


