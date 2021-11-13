from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#Seems that some degree of validation is disabled on sqlite 3
#So even with PositiveIntegerField, its a good sanity check
def validate_greater_than_zero(value):
    if (value <= 0):
        raise ValidationError(
            _('%(value) must be greater than zero'),
            params={'value': value},
        )