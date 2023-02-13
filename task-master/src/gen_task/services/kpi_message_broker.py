import json
import logging

from django.conf import settings
from pika import BlockingConnection
from pika.connection import URLParameters

logger = logging.getLogger(__name__)


class Message:
    def __init__(self, title: str, body: dict):
        self.title = title
        self.body = body

    def send(self):
        message = self._prepare_message()
        try:
            with KPIMessageBrokerService() as broker:
                broker.publish(message)
        except Exception as e:
            logger.error(f'Error while trying to send message {message} {e}')

    def _prepare_message(self):
        return {
            'title': self.title,
            'body': self.body
        }


class KPIMessageBrokerService:
    RABBITMQ_EXCHANGE = 'genesis.task.kpi'

    def __init__(self, rabbitmq_url=settings.RABBITMQ_URL):
        self.connection = BlockingConnection(URLParameters(rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.RABBITMQ_EXCHANGE, durable=True)
        self.channel.queue_declare(
            queue=settings.KPI_RABBITMQ_TITLE, durable=True
        )
        self.channel.queue_bind(
            exchange=self.RABBITMQ_EXCHANGE,
            queue=settings.KPI_RABBITMQ_TITLE, routing_key=''
        )

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.connection.close()

    def publish(self, message: dict):
        body = self._serialize_message(message)

        self.channel.basic_publish(
            self.RABBITMQ_EXCHANGE,
            '',
            body
        )

    def _serialize_message(self, message: dict):
        return json.dumps(message).encode()
