from django.db import models
from patient.models import Patient
from employee.models import Employee
from django.utils.translation import gettext_lazy as _

class Phone(models.Model):
  patient =models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name=('patient'))
  employee =models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=('employee'))
  phone_number = models.CharField(max_length=14, db_column='phone_number', verbose_name=('phone number'))
  description = models.TextField(db_column='description', verbose_name=('description'))
  
  class Meta: 
    db_table ='phone' 
    verbose_name = _('Phone')
    verbose_name_plural = _('Phones')

  def __str__(self):
    return self.phone_number+" "+self.patient.fist_name
