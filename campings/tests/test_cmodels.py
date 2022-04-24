from campings.models import Camping, Place, Reservation


def test_create_camping(db, user, place):
    """
    Test creating object of model Camping
    """
    camping = Camping.objects.create(owner=user, name='TestName', place=place)
    assert camping.name == 'TestName'


def test_reservation(db, user, camping):
    """
    Test creating object of model Reservation
    """
    Reservation.objects.create(check_in='2022-05-01', check_out='2022-05-05', people_number=3,
                               camping=camping)
    reservations = Reservation.objects.all()
    assert len(reservations) == 1


def test_place(db, user):
    """
    Test creating object of model Place
    """
    Place.objects.create(name='TestPlace')

    assert len(Place.objects.all()) == 1
