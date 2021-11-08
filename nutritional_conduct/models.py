from django.db import models
from antopometric_evaluation.models import AntopometricEvaluation
from smart_selects.db_fields import ChainedForeignKey
from diet_plan.models import DietPlan
from patient.models import Patient
from django.utils.translation import gettext_lazy as _

# Create your models here.
class NutritionalConduct(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name = _('patient'))
  antopometric_evaluation = ChainedForeignKey(AntopometricEvaluation, chained_field="patient", chained_model_field="patient", show_all = False, auto_choose = True, sort = True, verbose_name = _('antopomeetric_evaluation'))
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE, verbose_name = _('diet_plan'))
  description_nutricional_conduct= models.TextField(blank=True, db_column='description_nutricional_conduct', verbose_name = _('description_nutricional_conduct'))
  date_of_consultation=models.DateField( verbose_name = _('date_of_consultation'))

  EXERCISE_CHOICES = ( 
      ('L', _('Light')),
      ('M', _('Moderate')),
      ('I', _('Intensive')),
    )

  exercise_type = models.CharField(max_length=1, choices=EXERCISE_CHOICES, verbose_name = _('exercise'))

  def __str__(self):
    return self.patient.first_name + " " + self.patient.last_name
  class Meta:
    db_table ='nutricional_conduct'
    verbose_name = _('Nutricional Conduct')
    verbose_name_plural = _('Nutricional Conducts')

  def essential_calorie_basal(self):
    if (self.pk is None):
      return None
    age = (self.patient.birthday - self.date_of_consultation)
    if (self.patient.gender == 'F'):
      if (age in range(18, 30)):
        return (14.70 * float(self.antopometric_evaluation.weight) + 496)
      elif (age in range(30, 61)):
        return (8.70 * float(self.antopometric_evaluation.weight) + 829)
      else:
        return (10.5 * float(self.antopometric_evaluation.weight) + 596)
    else:
      if (age in range(18, 30)):
        return (15.3 * float(self.antopometric_evaluation.weight) + 679)
      elif (age in range(30, 61)):
        return (11.6 * float(self.antopometric_evaluation.weight) + 879)
      else:
        return (13.5 * float(self.antopometric_evaluation.weight) + 487)

  def activity_factor(self):
    if (self.pk is None):
      return None
    if (self.patient.gender == 'F'):
      if (self.exercise_type == 'L'):
        return 1.56
      elif (self.exercise_type == 'M'):
        return 1.64
      else:
        return 1.82
    else:
      if (self.exercise_type == 'L'):
        return 1.56
      elif (self.exercise_type == 'M'):
        return 1.78
      else:
        return 2.10

  def stringify_calory_need(self):
    ecb = self.essential_calorie_basal()
    factor = self.activity_factor()
    if (self.caloric_needs == None):
      return " "
    return str(ecb * factor)


  stringify_calory_need.short_description = _('caloric needs') 