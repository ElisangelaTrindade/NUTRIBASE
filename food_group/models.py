from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class FoodGroup(models.Model): 
  group = models.CharField(max_length=150,db_column='group', verbose_name = _('group'))
  calories = models.PositiveIntegerField(default=0, db_column='calories', verbose_name = _('calories'))

  def label_from_instance(self):
      return self.group

  def __str__(self):
    return self.group

  class Meta:
    db_table ='food_group' 
    verbose_name = _('Food Group')
    verbose_name_plural = _('Food Groups')

class Food(models.Model):
  food_group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE, verbose_name = _('food_group'))
  food_name = models.CharField(max_length=50, db_column='food_name', verbose_name = _('food_name'))
  protein = models.DecimalField(max_digits=8, decimal_places=2, db_column='protein', verbose_name = _('protein'))
  lipids = models.DecimalField(max_digits=8, decimal_places=2, db_column='lipids', verbose_name = _('lipids'))
  cholesterol = models.DecimalField(max_digits=8, decimal_places=2, db_column='cholesterol', verbose_name = _('cholesterol'))
  carbohydrates = models.DecimalField(max_digits=8, decimal_places=2, db_column='carbohydrates', verbose_name = _('carbohydrates'))
  dietary_fiber = models.DecimalField(max_digits=8, decimal_places=2, db_column='dietary_fiber', verbose_name = _('dietary_fiber'))
  iron = models.DecimalField(max_digits=8, decimal_places=2, db_column='iron', verbose_name = _('iron'))
  vitamin_c = models.DecimalField(max_digits=8, decimal_places=2, db_column='vitamin_C', verbose_name = _('vitamin_C'))
  calcium = models.DecimalField(max_digits=8, decimal_places=2, db_column='calcium', verbose_name = _('calcium'))
  calories = models.DecimalField(max_digits=8, decimal_places=2, db_column='calories', verbose_name = _('calories'))
  weight = models.DecimalField(max_digits=8, decimal_places=2, db_column='weight', verbose_name = _('weight'))


  def label_from_instance(self):
      return self.food_name

  def __str__(self):
    return self.food_name

  def calculate_calories_for(self, weight):
      return weight * self.food_group.calories / self.weight   

  class Meta:
    db_table ='food'
    verbose_name = _('Food')
    verbose_name_plural = _('Foods')
