from django.db import models
from patient.models import Patient

class Phone(models.Model):
  patient =models.ForeignKey(Patient, on_delete=models.CASCADE) 
  phone_number = models.CharField(max_length=14, db_column='phone_number')
  description = models.TextField(db_column='description')
  
  class Meta: 
    db_table ='phone' 
    def __str__(self):
      return self.phone_number
