from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class DietPlanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diet_plan'
    verbose_name = _('Diet Plan')
