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


  class Meta:
    db_table ='nutricional_conduct'
    verbose_name = _('Nutricional Conduct')
    verbose_name_plural = _('Nutricional Conducts')