from django.db import models
from diet_plan.models import DietPlan
from food_consumption.models import FoodConsumption, FoodIntolerance, FoodPreferences
from patient.models import Patient

# Create your models here.
class NutritionalConduct(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  food_intolerance = models.OneToOneField(FoodIntolerance, on_delete=models.CASCADE)
  food_preferences = models.OneToOneField(FoodPreferences, on_delete=models.CASCADE)
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
  food_consumption = models.ForeignKey(FoodConsumption, on_delete=models.CASCADE)
  caloric_needs = models.DecimalField(max_digits=8, decimal_places=3, db_column='caloric') 
  additional_information= models.TextField(db_column='additional_information')

  
  

  class Meta:
    db_table ='nutricional_conduct'