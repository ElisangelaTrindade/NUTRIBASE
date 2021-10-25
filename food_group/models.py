from django.db import models

# Create your models here.
class FoodGroup(models.Model): 
  group = models.CharField(max_length=150,db_column='group')
  calories = models.PositiveIntegerField(default=0, db_column='calories')

  class Meta:
    db_table ='food_group' 

class Food(models.Model):
  food_group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
  food_name = models.CharField(max_length=50, db_column='food_name')
  protein = models.DecimalField(max_digits=6, decimal_places=1, db_column='protein')
  lipids = models.DecimalField(max_digits=6, decimal_places=1, db_column='lipids')
  cholesterol = models.DecimalField(max_digits=6, decimal_places=1, db_column='cholesterol')
  carbohydrates = models.DecimalField(max_digits=6, decimal_places=1, db_column='carbohydrates')
  dietary_fiber = models.DecimalField(max_digits=6, decimal_places=1, db_column='dietary_fiber')
  iron = models.DecimalField(max_digits=6, decimal_places=1, db_column='iron')
  vitamin_c = models.DecimalField(max_digits=6, decimal_places=1, db_column='vitamin_C')
  calcium = models.DecimalField(max_digits=6, decimal_places=1, db_column='calcium')
  calories = models.DecimalField(max_digits=6, decimal_places=1, db_column='calories')
  weight = models.DecimalField(max_digits=6, decimal_places=1, db_column='weight')

  class Meta:
    db_table ='food' 


