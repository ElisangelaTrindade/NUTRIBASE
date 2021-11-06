from django.db import models
from patient.models import Patient
from user.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


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

  def __str__(self):
    return self.exercise_type.name

  class Meta:
    db_table ='exercise' 
    verbose_name = _('Exercise')
    verbose_name_plural = _('Exercises')

# nao gostei da ordem no admin