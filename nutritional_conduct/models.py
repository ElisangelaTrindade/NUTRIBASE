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
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE, verbose_name = _('diet_plan'), unique=True)
  description_nutricional_conduct= models.TextField(blank=True, db_column='description_nutricional_conduct', verbose_name = _('Nutricional Conduct'))
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
    unique_together = ['patient', 'antopometric_evaluation']
    db_table ='nutricional_conduct'
    verbose_name = _('Nutricional Conduct')
    verbose_name_plural = _('Nutricional Conducts')

  def essential_calorie_basal(self):
    if (self.pk is None or self.date_of_consultation  is None or self.patient.birthday is None):
      return None
    age = int((self.date_of_consultation - self.patient.birthday).days/365)
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
    if (ecb == None or factor == None):
      return " "
    return str(round(ecb * factor, 2))


  stringify_calory_need.short_description = _('caloric needs') 

  
  def calculate_bmi(self):
    if (self.pk is None):
      return None
    return self.antopometric_evaluation.weight / (self.antopometric_evaluation.height * self.antopometric_evaluation.height)
    
  def stringify_bmi(self):
    bmi = self.calculate_bmi()
    if (bmi == None  or self.date_of_consultation is None or self.patient.birthday is None):
      return ""
    
    age = int((self.date_of_consultation - self.patient.birthday).days/365)
    bmi = round(bmi, 2)
    type = _('Obesity 3')
    if ((age in range(18, 65))):
      if (bmi <= 16):
        type =  _('Underweight 3') 
      elif (bmi <= 17):
        type = _('Underweight 2')
      elif (bmi <= 18.5):
        type = _('Underweight 1')
      elif (bmi <= 25):
        type = _('Normal')
      elif (bmi <= 30):
        type = _('Overweight')
      elif (bmi <= 35):
        type = _('Obesity 1')
      elif (bmi <= 40):
        type = _('Obesity 2')
    if ((age in range(66, 100))):
      if (bmi<22):
        type = _('Underweight')
      elif (bmi<=27):
        type = _('Normal')
      else:
        type = _('Overweight')
    
    return  type + " - " + str(bmi)

  stringify_bmi.short_description= _('bmi')

  def stringify_cir_abdominal(self):
    type = _('Normal')
    if (self.patient.gender == 'F'):
      if float((self.antopometric_evaluation.abdomen_circumference>80)):
        type=_('High risk for cardiovascular disease ')
    else:
      if float((self.antopometric_evaluation.abdomen_circumference>94)):
        type=_('High risk of cardiovascular disease ')
    return  type 
  stringify_cir_abdominal.short_description=_('Abdominal circunference')

  
  
