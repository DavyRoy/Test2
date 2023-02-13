import dj_database_url
import pytest
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    DATABASE_URI = 'postgres://gen-task:7aw5AXSg@postgres:5432/gen-task_db'
    settings.DATABASES = {'default': dj_database_url.parse(DATABASE_URI, conn_max_age=600)}


pytest_plugins = [
    'gen_task.tests.fixtures'
]