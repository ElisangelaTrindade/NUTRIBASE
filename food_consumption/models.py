from django.db import models
from patient.models import Patient
from user.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class FoodConsumption(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name = _('patient'))
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('registered_by'))
  soft_drink = models.BooleanField (db_column='soft_drink', verbose_name = _('soft_drink'))
  candy = models.BooleanField(db_column='candy', verbose_name = _('candy'))
  deep_fried = models.BooleanField( db_column='deep_fried', verbose_name = _('deep_fried'))
  fast_food= models.BooleanField( db_column='fast_food', verbose_name = _('fast_food'))
  processed_food = models.BooleanField( db_column='processed_food', verbose_name = _('processed_food'))
  canned_food = models.BooleanField( db_column='canned', verbose_name = _('canned'))
  fruits = models.BooleanField( db_column='fruits', verbose_name = _('fruits'))
  vegetables = models.BooleanField( db_column='vegetables', verbose_name = _('vegetables'))
  others = models.TextField(blank=True, db_column='description', verbose_name = _('description'))
  

  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name
  

  class Meta:
    db_table ='food_consumption' 
    verbose_name = _('Food Consuption')
    verbose_name_plural = _('Food Consuptions')

class FoodIntolerance(models.Model):
  food_consumption = models.ForeignKey(FoodConsumption, on_delete=models.CASCADE, verbose_name = _('food_consumption'))
  intolerance_description= models.TextField(db_column='intolerance_description', verbose_name = _('intolerance_description'))

  def __str__(self):
    return self.intolerance_description
  
  
  class Meta:
    db_table ='food_intolerance' 
    verbose_name = _('Food Intolerance')
    verbose_name_plural = _('Food Intolerances')

class FoodPreferences(models.Model):
  food_consumption = models.ForeignKey(FoodConsumption, on_delete=models.CASCADE, verbose_name = _('food_consumption'))
  description= models.TextField(blank=True, db_column='description', verbose_name = _('description'))

  def __str__(self):
    return self.description

  class Meta:
    db_table ='food_preferences' 
    verbose_name = _('Food Preference')
    verbose_name_plural = _('Food Preferences')

