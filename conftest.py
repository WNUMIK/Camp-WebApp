import pytest


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """User instance from default django user model"""
    yield django_user_model.objects.create_user(email='a@a.pl', fullname='Ala', password='testPass123')
