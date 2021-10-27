from django.db import models
from patient.models import Patient
from user.models import User


# Create your models here.
class FoodConsumption(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  soft_drink = models.BooleanField (db_column='soft_drink')
  candy = models.BooleanField(db_column='candy')
  deep_fried = models.BooleanField( db_column='deep_fried')
  fast_food= models.BooleanField( db_column='fast_food')
  processed_food = models.BooleanField( db_column='processed_food')
  canned_food = models.BooleanField( db_column='canned')
  fruits = models.BooleanField( db_column='fruits')
  vegetables = models.BooleanField( db_column='vegetables')
  others = models.TextField(db_column='description')
  

  def label_from_instance(self):
      return self.patient.first_name+ " " +self.patient.last_name
  
  def __str__(self):
    return self.patient.first_name+ " " +self.patient.last_name

  class Meta:
    db_table ='food_consumption' 

class FoodIntolerance(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  intolerance_description= models.TextField(db_column='intolerance_description')

  def __str__(self):
    return self.patient.first_name + " " + self.patient.last_name

  class Meta:
    db_table ='food_intolerance' 

class FoodPreferences(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.TextField(db_column='description')

  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name
      
  class Meta:
    db_table ='food_preferences' 

