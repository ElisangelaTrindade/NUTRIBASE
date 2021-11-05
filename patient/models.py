from django.db import models
from cpffield import cpffield
from user.models import User
from location.models import City, State
from smart_selects.db_fields import ChainedForeignKey


class Patient(models.Model):
  first_name= models.CharField(blank=True, max_length=150, verbose_name='first name')
  last_name= models.CharField(blank=True, max_length=150, verbose_name='last name')
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
  cpf = cpffield.CPFField('CPF', max_length=11, unique=True)
  birthday = models.DateField()
  email = models.CharField(max_length=150,db_column='email_patient')
  street = models.CharField(max_length=50, db_column='street')
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  city = ChainedForeignKey(City, chained_field="state", chained_model_field="state", show_all = False, auto_choose = True, sort = True)
  zip_code = models.CharField(max_length=15,default = '', db_column='zip_code')

  GENDER_CHOICES = (
      ('M', 'Male'),
      ('F', 'Female'),
    )
    
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  
  def __str__(self):
        return self.first_name + " " + self.last_name
  
  class Meta:
    db_table ='patient'
 

 
  
  