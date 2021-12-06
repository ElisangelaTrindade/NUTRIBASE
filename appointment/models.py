from django.db import models
from django.utils.translation import gettext_lazy as _
from patient.models import Patient



class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name = _('patient'))
    date_of_consultation = models.DateTimeField(verbose_name = _('date_of_consultation'))
    duration = models.DurationField(_('duration (minutes)'), blank=False, null=False)
    reason = models.CharField(max_length=200,db_column='reason', verbose_name= _('reason'))

    class Meta: 
        db_table ='Appointment' 
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')

    def __str__(self):
        return self.patient.first_name + ' - ' + str(self.date_of_consultation)

