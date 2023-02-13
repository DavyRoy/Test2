import dj_database_url
import pytest
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    DATABASE_URI="postgres://gen_document_api:7aw5AXSg@localhost:5432/document_api_db"
    settings.DATABASES = {'default': dj_database_url.parse(DATABASE_URI, conn_max_age=600)}


pytest_plugins = [
    'gen_document.tests.fixtures'
]