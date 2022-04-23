from campings.models import Camping, Place, Reservation


def test_create_camping(db, user, place):
    camping = Camping.objects.create(owner=user, name='TestName', place=place)
    assert camping.name == 'TestName'


def test_reservation(db, user, camping):
    Reservation.objects.create(check_in='2022-05-01', check_out='2022-05-05', people_number=3,
                               camping=camping)
    reservations = Reservation.objects.all()
    assert len(reservations) == 1
