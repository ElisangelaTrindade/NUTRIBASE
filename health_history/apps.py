from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class HealthHistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'health_history'
    verbose_name = _('Health History')
