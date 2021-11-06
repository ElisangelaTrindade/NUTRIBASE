from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class FoodGroupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'food_group'
    verbose_name = _('Food Group')
    
