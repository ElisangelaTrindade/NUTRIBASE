from django.db import models
from patient.models import Patient
from user.models import User

# Create your models here.
class DietPlan(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.TextField(db_column='description')
  date_of_creation=models.DateField()
  amount_of_calories=models.DecimalField(max_digits=8, decimal_places=1, db_column='amount_of_calories')
  weigh=models.DecimalField(max_digits=8, decimal_places=1, db_column='weight')
  class Meta:
    db_table ='diet_plan' 
  