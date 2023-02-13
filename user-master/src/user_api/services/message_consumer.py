import json
import logging
import threading

from django.conf import settings
from pika import BlockingConnection, URLParameters

from user_api.services import KPIHandler

logging.getLogger("pika").propagate = False

class MessageConsumer:
    CALLBACK_BY_TITLE = {
        settings.KPI_TITLE: lambda message: KPIHandler(message)(),

    }

    def __init__(self, rabbitmq_url=settings.RABBITMQ_URL):
        self.rabbitmq_url = rabbitmq_url
        self._init_logger()
        self._init_rabbitmq_connection()
        self._init_task_kpi_channel()

    @staticmethod
    def _serialize_message(message: str) -> dict:
        return json.loads(message)


    def _init_logger(self):
        logging.basicConfig(level=logging.INFO)

        self.logger = logging.getLogger(__name__)


    def _init_rabbitmq_connection(self):
        self.connection = BlockingConnection(URLParameters(self.rabbitmq_url))

    def _init_task_kpi_channel(self):
        self.task_kpi_channel = self.connection.channel()

        self.task_kpi_channel.basic_consume(
            settings.KPI_TITLE,
            self._callback,
            auto_ack=True
        )

    def start(self):
        self.logger.info('Start consuming')
        threading.Thread(target=self.task_kpi_channel.start_consuming()).start()


    def _callback(self, ch, method, properties, body):
        try:
            data = self._serialize_message(body)
            title, message = data.get('title'), data.get('body')
            if (callback_service := self.CALLBACK_BY_TITLE.get(title, None)) is not None:
                callback_service(message)

        except Exception as e:

            self.logger.error(f'error while consuming messages {e} {message}')