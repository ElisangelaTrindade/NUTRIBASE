from django.db import models

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
  class Meta:
    db_table ='food_consumption' 

class FoodIntolerance(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  intolerance_description= models.TextField(db_column='intolerance_description')
  class Meta:
    db_table ='food_intolerance' 

class FoodPreferences(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.TextField(db_column='description')
  class Meta:
    db_table ='food_preferences' 
