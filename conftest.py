import pytest

from campings.models import Place, Camping


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """User instance from default django user model"""
    yield django_user_model.objects.create_user(email='a@a.pl', fullname='Ala', password='testPass123')


@pytest.fixture(scope='function')
def place(user):
    """Place instance from place model"""
    yield Place.objects.create(name='TestPlace')


@pytest.fixture(scope='function')
def camping(user, place):
    """Camping instance from camping model"""
    yield Camping.objects.create(name='Test', owner=user, place=place)
