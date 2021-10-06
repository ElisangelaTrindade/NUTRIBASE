from django.db import models

# Create your models here.
class ClinicEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  nails= models.CharField(max_length=100, db_column='nails')
  skin = models.CharField(max_length=100, db_column='skin')
  bladder_habits = models.CharField(max_length=100, db_column='bladder_habits')
  bowel_habits = models.CharField(max_length=100, db_column='bowel_habits') 
  additional_information= models.TextField(db_column='additional_information')
  date_of_consultation=models.DateField()
  updated=models.DateField()
  class Meta:
    db_table ='clinic_evaluation' 

class GastrointestinalTractSymptoms(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  dysphagia = models.BooleanField (db_column='dysphagia')
  pain= models.BooleanField(db_column='pain')
  reflux = models.BooleanField( db_column='reflux')
  heart_burn= models.BooleanField( db_column='heart_burn')
  constipation = models.BooleanField( db_column='constipation')
  nausea= models.BooleanField( db_column='nausea')
  diarrhea= models.BooleanField( db_column='diarrhea')
  others = models.TextField(db_column='description')
  class Meta:
    db_table ='gastrointestinalt_tract_symptoms' 