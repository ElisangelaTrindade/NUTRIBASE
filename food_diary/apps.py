from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FoodDiaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'food_diary'
    verbose_name = _('Food Diary')
