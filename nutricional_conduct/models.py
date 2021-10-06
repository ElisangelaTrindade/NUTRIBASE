from django.db import models
from diet_plan.models import DietPlan
from food_comsuption.models import FoodConsumption, FoodIntolerance
from user.models import User
from patient.models import Patient

# Create your models here.
class NutritionalConduct(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  food_intolerance = models.OneToOneField(FoodIntolerance, on_delete=models.CASCADE)
  food_preferences = models.OneToOneField(User, on_delete=models.CASCADE)
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
  food_consumption = models.ForeignKey(FoodConsumption, on_delete=models.CASCADE)
  caloric_needs = models.DecimalField(max_digits=4, decimal_places=2, db_column='caloric') 
  additional_information= models.TextField(db_column='additional_information')

  class Meta:
    db_table ='nutricional_information'