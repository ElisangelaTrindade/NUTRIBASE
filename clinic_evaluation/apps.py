from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClinicEvaluationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clinic_evaluation'
    verbose_name = _('Clinic Evaluation')
    #Avaliação Clínica
