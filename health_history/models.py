from django.db import models
from patient.models import Patient
from user.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class PatientHealthHistory(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name = _('patient'))
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = _('registered_by'))
  obesity = models.BooleanField(db_column='obesity', verbose_name = _('obesity'))
  cardiovascular_disease = models.BooleanField( db_column='cardiovascular_disease', verbose_name = _('cardiovascular_disease'))
  hypertension = models.BooleanField(db_column='hypertension', verbose_name = _('hypertension'))
  cancer = models.BooleanField(db_column='cancer', verbose_name = _('cancer'))
  diabetes = models.BooleanField( db_column='diabetes', verbose_name = _('diabetes'))
  dyslipidemia = models.BooleanField(db_column='dyslipidemia', verbose_name = _('dyslipidemia'))
  others = models.TextField (blank= True, db_column='others', verbose_name = _('other'))

  def __str__(self):
    return self.patient.first_name + " " + self.patient.last_name
  
  class Meta:
    db_table ='patient_health_history' 
    verbose_name = _('Patient Health History')
    verbose_name_plural = _('Patient Health Histories')

class FamilyHealthHistory(models.Model):
  patient_health_history= models.ForeignKey(PatientHealthHistory, on_delete=models.CASCADE, verbose_name = _('patient_health_history'))
  obesity = models.BooleanField(db_column='obesity', verbose_name = _('obesity'))
  cardiovascular_disease = models.BooleanField( db_column='cardiovascular_disease', verbose_name = _('cardiovascular_disease'))
  hypertension = models.BooleanField (db_column='hypertension', verbose_name = _('hypertension'))
  cancer = models.BooleanField (db_column='cancer', verbose_name = _('cancer'))
  diabetes = models.BooleanField (db_column='diabetes', verbose_name = _('diabetes'))
  dyslipidemia = models.BooleanField(db_column='dyslipidemia', verbose_name = _('dyslipidemia'))
  others = models.TextField(blank=True, db_column='others', verbose_name = _('others'))
  
  class Meta:
    db_table ='family_health_history'  
    verbose_name = _('Family Health History')
    verbose_name_plural = _('Family Health Histories')

