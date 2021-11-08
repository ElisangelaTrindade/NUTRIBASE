from django.db import models
from diet_plan.models import DietPlan
from food_consumption.models import FoodConsumption, FoodIntolerance, FoodPreferences
from patient.models import Patient
from django.utils.translation import gettext_lazy as _

# Create your models here.
class NutritionalConduct(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name = _('patient'))
  food_intolerance = models.OneToOneField(FoodIntolerance, on_delete=models.CASCADE, verbose_name = _('food_intolerance'))
  food_preferences = models.OneToOneField(FoodPreferences, on_delete=models.CASCADE, verbose_name = _('food_preferences'))
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE, verbose_name = _('diet_plan'))
  food_consumption = models.ForeignKey(FoodConsumption, on_delete=models.CASCADE, verbose_name = _('food_consumption'))
  caloric_needs = models.DecimalField(max_digits=8, decimal_places=3, db_column='caloric', verbose_name = _('caloric_needs'))
  additional_information= models.TextField(blank=True, db_column='additional_information', verbose_name = _('additional_information'))
  date_of_consultation=models.DateField( verbose_name = _('date_of_consultation'))

  class Meta:
    db_table ='nutricional_conduct'
    verbose_name = _('Nutricional Conduct')
    verbose_name_plural = _('Nutricional Conducts')

  def essential_calorie_basal(self):
    if (self.pk is None):
      return None
    age = self.patient.birthday - self.date_of_consultation
    if (self.patient.gender == 'F'):
      if (age in range(18, 30)):
        return (14.70 * self.patient.weight+496)
      elif (age in range(30, 61)):
        return (8.70 * self.patient.weight+829)
      else:
        return (10.5 * self.patient.weight+596)
    else:
      if (age in range(18, 30)):
        return (15.3 * self.patient.weight+679)
      elif (age in range(30, 61)):
        return (11.6 * self.patient.weight+879)
      else:
        return (13.5 * self.patient.weight+487)

  def stringify_ecb(self):
    ecb = self.essential_calorie_basal()
    if (ecb == None):
      return ""
    return str(ecb)

    

  stringify_ecb.short_description = _('Bmi')

  def essential_calorie_basal(self):
    if (self.pk is None):
      return None
    age = self.patient.birthday - self.date_of_consultation
    if (self.patient.gender == 'F'):
      if (age in range(18, 30)):
        return (14.70 * self.patient.weight+496)
      elif (age in range(30, 61)):
        return (8.70 * self.patient.weight+829)
      else:
        return (10.5 * self.patient.weight+596)
    else:
      if (age in range(18, 30)):
        return (15.3 * self.patient.weight+679)
      elif (age in range(30, 61)):
        return (11.6 * self.patient.weight+879)
      else:
        return (13.5 * self.patient.weight+487)

  def stringify_ecb(self):
    ecb = self.essential_calorie_basal()
    if (ecb == None):
      return ""
    return str(ecb)