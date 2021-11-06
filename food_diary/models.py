from django.db import models
from patient.models import Patient
from user.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class FoodDiary(models.Model):
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = _('registered_by'))
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name = _('patient'))
  description= models.TextField(db_column='description', verbose_name = _('description'))
  date_of_consultation=models.DateField(verbose_name = _('date_of_consultation'))
  
  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name
  
  class Meta:
    db_table ='food_diary'
    verbose_name = _('Food Diary')
    verbose_name_plural = _('Food Diaries')
