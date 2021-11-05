from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AntopometricEvaluationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'antopometric_evaluation'
    verbose_name = _('Avaliação antropométrica')