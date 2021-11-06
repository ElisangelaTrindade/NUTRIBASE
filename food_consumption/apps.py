from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FoodConsumptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'food_consumption'
    verbose_name = _('Food Comsuption')