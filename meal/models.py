from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from diet_plan.models import DietPlan
from food_diary.models import FoodDiary
from food_group.models import Food
from user.models import User

# Create your models here.
class Meal(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  #food_diary = models.ForeignKey(FoodDiary, on_delete=models.CASCADE)
  #diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
  type_meal = models.CharField(max_length=50,db_column='type_meal')
  time_meal = models.DateTimeField(db_column='time_meal')
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')

  def __str__(self):
    return self.type_meal

  class Meta:
    db_table ='meal'

class MealFood (models.Model):
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
  weight = models.DecimalField(max_digits=8, decimal_places=1, db_column='weight')

  class Meta:
    db_table ='meal_food' 
