import redis
from django.conf import settings

redis_client = redis.Redis(host=settings.KEYDB_HOST, port=settings.KEYDB_PORT, db=settings.KEYDB_DB, password=settings.KEYDB_PASSWORD)
