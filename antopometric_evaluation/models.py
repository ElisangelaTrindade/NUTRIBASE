from django.db import models
from patient.models import Patient
from user.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class AntopometricEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name =_('patient'))
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = _('registered_by'))
  weight = models.DecimalField(max_digits=6, decimal_places=2, db_column='weight', verbose_name = _('weight')) 
  height = models.DecimalField(max_digits=4, decimal_places=2, db_column='height', verbose_name = _('height'))

  BMI = models.DecimalField(max_digits=4, decimal_places=2, db_column='ibm', verbose_name = _('bmi'))
  arm_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='arm_circumference', verbose_name = _('arm_circumference')) 
  abdomen_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='abdomen_circumference', verbose_name = _('abdomen_circumference')) 
  wrist_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='wrist_circumference', verbose_name = _('wrist_circumference'))
  date_of_consultation=models.DateField( verbose_name = _('date_of_consultation'))
  updated=models.DateField(verbose_name = _('updated'))
  additional_information= models.TextField(blank=True, db_column='additional_information',verbose_name = _('additional_information'))
 
  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.User.id
    obj.save()

  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name
  
  class Meta:
    db_table ='antopometric_evaluation' 
    verbose_name = _('Antopometric Evaluation')
    verbose_name_plural = _('Antopometric Evaluations')

  def calculate_bmi(self):
    if (self.pk is None):
      return None
    return self.weight / (self.height * self.height)
    
  def stringify_bmi(self):
    bmi = self.calculate_bmi()
    if (bmi == None):
      return ""

    if (bmi <= 16):
      return _('Underweight 3'),
    elif (bmi <= 17):
      return _('Underweight 2')
    elif (bmi <= 18.5):
      return _('Underweight 1')
    elif (bmi <= 25):
      return _('Normal')
    elif (bmi <= 30):
      return _('Overweight')
    elif (bmi <= 35):
      return _('Obesity')
    elif (bmi <= 40):
      return _('Obesity 2')
    #bmi > 40
    return _('Obesity 3')

  stringify_bmi.short_description = _('Bmi')

