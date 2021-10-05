from django.db import models

# Create your models here.
class FoodGroup(models.Model): 
  group = models.CharField(max_length=150,db_column='group')
  weight = models.DecimalField(max_digits=8, decimal_places=1, db_column='weight')
  calories = models.PositiveIntegerField(default=0, db_column='calories')

  class Meta:
    db_table ='food_group' 

class Food(models.Model):
  food_group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
  diet_plan = models.OneToOneField(DietPlan, on_delete=models.CASCADE)
  food_name=models.CharField(max_length=50, db_column='food_name')
  weigh=models.DecimalField(max_digits=8, decimal_places=1, db_column='weight')
  
  class Meta:
    db_table ='food' 