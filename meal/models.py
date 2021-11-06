from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from food_group.models import Food
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Meal(models.Model):
  type_meal = models.CharField(max_length=50,db_column='type_meal', verbose_name = _('type_meal'))
  time_meal = models.DateTimeField(db_column='time_meal', verbose_name = _('time_meal'))
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name = _('content_type'))
  object_id = models.PositiveIntegerField(verbose_name = _('object_id'))
  content_object = GenericForeignKey('content_type', 'object_id')

  class Meta:
    db_table ='meal'
    verbose_name = _('Meal')
    verbose_name_plural = _('Meals')



class MealFood (models.Model):
  food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name = _('food'))
  meal = models.ForeignKey(Meal, on_delete=models.CASCADE, verbose_name = _('meal'))
  weight = models.DecimalField(max_digits=8, decimal_places=1, db_column='weight', verbose_name = _('weight'))

  def test():
    return 10

  class Meta:
    db_table ='meal_food' 
    verbose_name = _('Meal Foods')
    verbose_name_plural = _('Meal Foods')

  
  

  

