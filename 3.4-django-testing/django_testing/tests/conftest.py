import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from django_testing.settings import MAX_STUDENTS_PER_COURSE


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def courses_factory():
    def factory(**kwargs):
        return baker.make('Course', **kwargs)
    return factory


@pytest.fixture()
def students_factory():
    def factory(**kwargs):
        return baker.make('Student', **kwargs)
    return factory
