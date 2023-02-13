from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Type(IntegerChoices):
    issue = 0, _('Issue')
    assignment = 1, _('Assignment')
    agreement = 2, _('Agreement')
    sos = 3, _('SOS')

    @classmethod
    def get_value(cls, index: int) -> str:
        return cls.choices[index][1]
