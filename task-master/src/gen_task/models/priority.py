from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Priority(IntegerChoices):
    high = 0, _('High')
    medium = 1, _('Medium')
    low = 2, _('Low')

    @classmethod
    def get_value(cls, index: int) -> str:
        return cls.choices[index][1]
