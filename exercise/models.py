from django.db import models
from patient.models import Patient
from user.models import User

class ExerciseType(models.Model):
  name = models.CharField(max_length=255, db_column='type')

 
class Meta:
  db_table ='exercise_type' 

class Exercise(models.Model):
  exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  frequency = models.CharField(max_length=255, db_column='frequency')

def __str__(self):
  return self.exercisetype.name

class Meta:
    db_table ='exercise' 

# nao gostei da ordem no admin