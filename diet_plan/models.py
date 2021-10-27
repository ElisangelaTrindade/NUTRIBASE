from django.db import models
from patient.models import Patient
from user.models import User
from food_group.models import Food

# Create your models here.
class DietPlan(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.TextField(db_column='description')
  date_of_creation=models.DateField()
  diet_food=models.ManyToManyField(Food,  through=u"DietFood", related_name=u'diet_foods')

  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name

  class Meta:
    db_table ='diet_plan' 
  
class DietFood (models.Model):
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  diet = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
  weight = models.DecimalField(max_digits=8, decimal_places=1, db_column='weight')

  class Meta:
    db_table ='diet_food' 