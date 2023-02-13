import pytest
from document.tests.fixtures_factory import DocumentFactory, TypeDocumentFactory


_ = pytest.fixture(autouse=True)(lambda db: None)


@pytest.fixture()
def document():
    return DocumentFactory.create()


@pytest.fixture()
def type_document():
    return TypeDocumentFactory.create()
