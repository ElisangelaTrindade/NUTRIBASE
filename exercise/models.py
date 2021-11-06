from django.db import models
from patient.models import Patient
from user.models import User
from django.utils.translation import gettext_lazy as _

class ExerciseType(models.Model):
  name = models.CharField(max_length=255, db_column='type', verbose_name = _('name_exercise'))

  class Meta:
    #db_table ='exercise_type' 
    verbose_name = _('Exercise')
    verbose_name_plural = _('Exercises')


class Exercise(models.Model):
  exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE, verbose_name = _('exercise_type'))
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE,  verbose_name = _('patient'))
  frequency = models.CharField(max_length=255, db_column='frequency', verbose_name = _('frequency'))

  def __str__(self):
    return self.exercisetype.name

  class Meta:
    db_table ='exercise' 
    verbose_name = _('Exercise')
    verbose_name_plural = _('Exercises')

# nao gostei da ordem no admin