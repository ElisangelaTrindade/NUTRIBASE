from django.db import models
from patient.models import Patient
from user.models import User
from meal.models import Meal
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from nutribase.validators import validate_greater_than_zero

# Create your models here.
class DietPlan(models.Model):
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = _('registered_by'))
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name = _('patient'))
  description= models.TextField(db_column='description', verbose_name = _('description'))
  date_of_creation=models.DateField(verbose_name = _('date_of_creation'))

  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name

  class Meta:
    db_table ='diet_plan' 
    verbose_name = _('Diet Plan')
    verbose_name_plural = _('Diet Plans')

  def calculate_total_of_calories(self):
    #We rely here on another select, this is due to the content_type_id dependency lacking a meal_set
    meals = Meal.objects.filter(object_id = self.id, content_type_id = ContentType.objects.get_for_model(self).id, validators=[validate_greater_than_zero])
    total = 0
    for meal in meals:
       for mealfood in meal.mealfood_set.all():
         total += mealfood.calculate_calories()
    
    return round(total, 2)