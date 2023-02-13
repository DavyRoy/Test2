from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Status(IntegerChoices):
    created = 0, _('Created')
    processing = 1, _('Processing')
    on_pause = 2, _('On pause')
    on_review = 3, _('On review')
    returned = 4, _('Returned')
    agreed = 5, _('Agreed')
    finished = 6, _('Finished')
    archived = 7, _('Archived')

    @classmethod
    def get_value(cls, index: int) -> str:
        return cls.choices[index][1]
