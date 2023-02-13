import random
from decimal import Decimal
import factory.fuzzy

from factory import Faker, LazyFunction, Sequence, SubFactory
from factory.django import DjangoModelFactory

from user_api.models import User, Role


class RoleFactory(DjangoModelFactory):
    id = Faker('uuid')
    name = Faker('word')
    priority = False
    is_default = False

    class Meta:
        model = Role


class UserFactory(DjangoModelFactory):
    avatar = None
    username = Sequence(lambda n: n)
    first_name = Faker('word')
    last_name = Faker('word')
    kpi = LazyFunction(lambda: Decimal(str(random.randint(100000000, 9999999999) / 10000000)))
    role = SubFactory(RoleFactory)
    phone = '+79991234567'

    @factory.post_generation
    def role(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for role in extracted:
                self.role.add(role)

    class Meta:
        model = User


