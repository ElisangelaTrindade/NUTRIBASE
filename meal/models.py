from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from food_group.models import Food


# Create your models here.
class Meal(models.Model):
  type_meal = models.CharField(max_length=50,db_column='type_meal')
  time_meal = models.DateTimeField(db_column='time_meal')
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')

  class Meta:
    db_table ='meal'


class MealFood (models.Model):
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
  weight = models.DecimalField(max_digits=8, decimal_places=1, db_column='weight')

  def test():
    return 10

  class Meta:
    db_table ='meal_food' 

  
  

  

