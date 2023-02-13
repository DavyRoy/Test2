import pytest

_ = pytest.fixture(autouse=True)(lambda db: None)

