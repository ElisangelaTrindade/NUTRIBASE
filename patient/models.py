from django.db import models
from cpf_field.models import CPFField
from user.models import User
from location.models import City, State
from smart_selects.db_fields import ChainedForeignKey
from django.utils.translation import gettext_lazy as _


class Patient(models.Model):
  first_name= models.CharField(blank=True, max_length=150, verbose_name=_('first name'))
  last_name= models.CharField(blank=True, max_length=150, verbose_name=_('last name'))
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = _('registered_by'))
  cpf = CPFField('CPF',max_length=14, unique=True)
  birthday = models.DateField(verbose_name = _('birthday'))
  email = models.CharField(max_length=150,db_column='email_patient', verbose_name = _('email'))
  street = models.CharField(max_length=50, db_column='street', verbose_name = _('street'))
  state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name = _('state'))
  city = ChainedForeignKey(City, chained_field="state", chained_model_field="state", show_all = False, auto_choose = True, sort = True, verbose_name = _('city'))
  zip_code = models.CharField(max_length=15,default = '', db_column='zip_code', verbose_name = _('zip code'))

  GENDER_CHOICES = ( 
      ('M', _('Male')),
      ('F', _('Female')),
    )
  

  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name = _('gender'))
  
  def __str__(self):
        return self.first_name + " " + self.last_name
  
  class Meta:
    db_table ='patient'
    verbose_name = _('Patient')
    verbose_name_plural = _('Patients')
 

 
  
  