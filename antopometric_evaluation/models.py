from django.db import models
from patient.models import Patient
from user.models import User
from django.utils.translation import gettext_lazy as _
from nutribase.validators import validate_greater_than_zero

# Create your models here.
class AntopometricEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name =_('patient'))
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = _('registered_by'))
  weight = models.DecimalField(max_digits=6, decimal_places=2, db_column='weight', verbose_name = _('weight'), validators=[validate_greater_than_zero]) 
  height = models.DecimalField(max_digits=4, decimal_places=2, db_column='height', verbose_name = _('height'), validators=[validate_greater_than_zero])
  arm_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='arm_circumference', verbose_name = _('arm_circumference'), validators=[validate_greater_than_zero]) 
  abdomen_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='abdomen_circumference', verbose_name = _('abdomen_circumference'), validators=[validate_greater_than_zero]) 
  wrist_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='wrist_circumference', verbose_name = _('wrist_circumference'), validators=[validate_greater_than_zero])
  date_of_consultation=models.DateField( verbose_name = _('date_of_consultation'))
  updated=models.DateField(verbose_name = _('updated'))
  additional_information= models.TextField(blank=True, db_column='additional_information',verbose_name = _('additional_information'))
 
  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.User.id
    obj.save()

  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name + " " + str(self.updated)
  
  class Meta:
    db_table ='antopometric_evaluation' 
    verbose_name = _('Antopometric Evaluation')
    verbose_name_plural = _('Antopometric Evaluations')
