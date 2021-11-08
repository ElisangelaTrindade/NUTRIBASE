from django.db import models
from patient.models import Patient
from user.models import User
from django.utils.translation import gettext_lazy as _


class ExerciseType(models.Model):
  name = models.CharField(max_length=255, db_column='type', verbose_name = _('name_exercise'))
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name = _('registered_by'))

  class Meta:
    #db_table ='exercise_type' 
    verbose_name = _('Exercise')
    verbose_name_plural = _('Exercises')

  def __str__(self):
    return self.name


class Exercise(models.Model):
  exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE, verbose_name = _('exercise_type'))
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE,  verbose_name = _('patient'))
  frequency = models.CharField(max_length=255, db_column='frequency', verbose_name = _('frequency'))
  light_intensity = models.BooleanField (db_column='light_intensity', verbose_name = _('light_intensity'))
  moderate_intensity  = models.BooleanField(db_column='moderate_intensity', verbose_name = _('moderate_intensity'))
  high_intensity = models.BooleanField( db_column='high_intensity', verbose_name = _('high_intensity'))

  def __str__(self):
    return self.exercise_type.name 

  class Meta:
    db_table ='exercise' 
    verbose_name = _('Exercise')
    verbose_name_plural = _('Exercises')

# nao gostei da ordem no admin