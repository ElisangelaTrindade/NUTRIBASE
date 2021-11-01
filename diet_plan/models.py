from django.db import models
from patient.models import Patient
from user.models import User

# Create your models here.
class DietPlan(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.TextField(db_column='description')
  date_of_creation=models.DateField()

  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name

  class Meta:
    db_table ='diet_plan' 
  

