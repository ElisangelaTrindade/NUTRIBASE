from django.db import models
from cpffield import cpffield
from django.conf import settings
from location.models import City, State
from user.models import User
from smart_selects.db_fields import ChainedForeignKey

class Employee(models.Model):
  user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user'
  )
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_by')
  hire_date = models.DateField(db_column='hire_date')
  cpf = cpffield.CPFField('CPF', max_length=14, unique=True)
  birthday = models.DateField()
  email = models.CharField(max_length=150,db_column='email_patient')
  street = models.CharField(max_length=50, db_column='street')
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  city = ChainedForeignKey(City, chained_field="state", chained_model_field="state", show_all = False, auto_choose = True, sort = True)
  zip_code = models.CharField(max_length=9,default = '')

  def label_from_instance(self):
      return self.user.first_name+ " " +self.user.last_name
  
  def __str__(self):
    return self.user.first_name+ " " +self.user.last_name
  

  class Meta:
    db_table ='employee'

