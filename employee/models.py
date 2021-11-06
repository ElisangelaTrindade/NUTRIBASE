from django.db import models
from cpffield import cpffield
from django.conf import settings
from location.models import City, State
from user.models import User
from smart_selects.db_fields import ChainedForeignKey
from django.utils.translation import gettext_lazy as _

class Employee(models.Model):
  user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user'
  )
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_by', verbose_name = _('registered_by'))
  hire_date = models.DateField(db_column='hire_date', verbose_name = _('hire_date'))
  cpf = cpffield.CPFField('CPF', max_length=14, unique=True)
  birthday = models.DateField(verbose_name = _('birthday'))
  email = models.CharField(max_length=150,db_column='email_patient', verbose_name = _('email'))
  street = models.CharField(max_length=50, db_column='street', verbose_name = _('address'))
  state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name = _('state'))
  city = ChainedForeignKey(City, chained_field="state", chained_model_field="state", show_all = False, auto_choose = True, sort = True, verbose_name = _('city'))
  zip_code = models.CharField(max_length=9,default = '', verbose_name = _('zip code'))

  def label_from_instance(self):
      return self.user.first_name+ " " +self.user.last_name
  
  def __str__(self):
    return self.user.first_name+ " " +self.user.last_name
  

  class Meta:
    db_table ='employee'
    verbose_name = _('Employee')
    verbose_name_plural = _('Employees')

