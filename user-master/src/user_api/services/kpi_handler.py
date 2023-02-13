import logging

from user_api.models import User

class KPIHandler:
    def __init__(self, message: dict) -> None:
        self.message = message
        self._deserialize_message()
        self.logger = logging.getLogger(__name__)

    def _deserialize_message(self):
        self.user_id = self.message.get('user_id')
        self.kpi = self.message.get('kpi')

    def _update_kpi(self):
        User.objects.filter(id=self.user_id).update(kpi=self.kpi)
        self.logger.debug('user kpi updated sucsesfull')
        

    def __call__(self, *args, **kwargs):
        self._update_kpi()