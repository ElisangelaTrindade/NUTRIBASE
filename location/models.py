from django.db import models
from django.utils.translation import gettext_lazy as _

class State(models.Model):
  name = models.CharField(max_length=50,db_column='state', verbose_name = _('state'))
  acrm= models.CharField(max_length=3,db_column='acrm', verbose_name = _('acrm'))
  
  def label_from_instance(self):
      return self.name
  
  def __str__(self):
    return self.name 
  
  class Meta:
    db_table ='state'
    
class City(models.Model):
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  city = models.CharField(max_length=100, db_column='city', verbose_name = _('city'))

  def __str__(self):
    return self.city
  
  class Meta:
    db_table ='city'



