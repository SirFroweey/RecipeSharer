from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valid_quantity(value):
    if value < 1:
        raise ValidationError(
            _('%(value)s must be greater than 0'),
            params={'value': value},
        )


def valid_tags(value):
    if value.find(',') < 0:
        raise ValidationError(
            _('%(value)s must contain comma seperated values'),
            params={'value': value},
        )
