import pytest

from campings.models import Camping, Place, Reservation


@pytest.mark.django_db
def test_add_camping(user, django_user_model):
    owner = django_user_model.objects.create_user(email='t@t.pl', fullname='TestUser', password='testPass123')
    place = Place.objects.create(name='TestPlace')
    camping = Camping.objects.create(owner=owner, name='TestName', place=place)
    assert camping.name == 'TestName'


@pytest.mark.django_db
def test_reservation(user, django_user_model):
    owner = django_user_model.objects.create_user(email='t@t.pl', fullname='TestUser', password='testPass123')
    place = Place.objects.create(name='TestPlace')
    camping = Camping.objects.create(owner=owner, name='TestName', place=place)
    reservation = Reservation.objects.create(check_in='2022-05-01', check_out='2022-05-05', people_number=3, camping=camping)
    reservations = Reservation.objects.all()
    assert len(reservations) == 1
