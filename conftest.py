import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group

from campings.models import Place, Camping, Reservation


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """User instance from default django user model"""
    yield django_user_model.objects.create_user(email='a@a.pl', fullname='Ala', password='testPass123')


@pytest.fixture
def regular_user(db):
    user = get_user_model().objects.create(email='pytest@tester.py', fullname='Pytester', is_active=True)
    user.set_password('pytest')
    user.save()
    permission = Permission.objects.get(name='Can view camping')
    regular_group = Group.objects.get(name='regular')
    user.groups.add(regular_group)
    user.user_permissions.add(permission)
    return user


@pytest.fixture(scope='function')
def place(user):
    """Place instance from place model"""
    yield Place.objects.create(name='TestPlace')


@pytest.fixture(scope='function')
def camping(user, place):
    """Camping instance from camping model"""
    yield Camping.objects.create(name='Test', owner=user, place=place)


@pytest.fixture
def logged_user(regular_user, client):
    yield client.login(email='pytest@tester.py', password='pytest')


@pytest.fixture
def create_reservation(regular_user, db, camping):
    yield Reservation.objects.create(camping=camping, check_in='2022-01-05', check_out='2022-02-05', people_number=5)
