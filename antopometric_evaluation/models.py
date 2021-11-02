from django.db import models
from patient.models import Patient
from user.models import User

# Create your models here.
class AntopometricEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
  weight = models.DecimalField(max_digits=6, decimal_places=2, db_column='weight') 
  height = models.CharField(max_length=4,db_column='height')
  BMI = models.DecimalField(max_digits=4, decimal_places=2, db_column='ibm')
  arm_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='arm_circumference') 
  abdomen_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='abdomen_circumference') 
  wrist_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='wrist_circumference')
  date_of_consultation=models.DateField()
  updated=models.DateField()
  additional_information= models.TextField(blank=True, db_column='additional_information')
 
  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.User.id
    obj.save()

  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name
  
  class Meta:
    db_table ='antopometric_evaluation' 
