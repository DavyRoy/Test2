from factory import Faker, SubFactory
from factory.django import FileField, DjangoModelFactory
from document.models import Document, TypeDocument


class TypeDocumentFactory(DjangoModelFactory):
    id = Faker('uuid4')
    name = Faker('name')
    activity = False
    created_by = Faker('uuid4')
    updated_by = Faker('uuid4')
    created_at = Faker('date_time')
    updated_at = Faker('date_time')

    class Meta:
        model = TypeDocument


class DocumentFactory(DjangoModelFactory):
    id = Faker('uuid4')
    name_document = Faker("word")
    type = SubFactory(TypeDocumentFactory)
    preview_image = None
    file = FileField(filename=f'{Faker("word")}.pdf')
    is_archive = False
    created_by = Faker('uuid4')
    updated_by = Faker('uuid4')
    created_at = Faker('date_time')
    updated_at = Faker('date_time')

    class Meta:
        model = Document
