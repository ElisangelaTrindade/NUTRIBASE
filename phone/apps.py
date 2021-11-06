from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PhoneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phone'
    verbose_name=_('Phone number')
