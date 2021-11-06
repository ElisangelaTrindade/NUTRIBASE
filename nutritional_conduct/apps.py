from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NutritionalConductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nutritional_conduct'
    verbose_name = _('Nutritional Conduct')
