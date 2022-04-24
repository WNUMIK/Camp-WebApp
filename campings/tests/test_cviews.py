import pytest
from django.urls import reverse
from campings.views import CampingDetailView


def test_camping_detail_view(rf, user, camping):
    """
    Test detail view of model camping
    """
    kwargs_camping = {'slug': camping.slug}
    url = reverse('campings:detail-camping', kwargs=kwargs_camping)
    request = rf.get(url)
    response = CampingDetailView.as_view()(request, **kwargs_camping)

    assert response.status_code == 200


def test_add_camping_permission(client):
    """
    Test permission of not logged user
    """
    url = reverse('campings:create-camping')
    response = client.get(url)

    assert response.status_code == 403


def test_reservation_permission(client):
    """
    Test permission of not logged user
    """
    url = reverse('campings:reserve-camping')
    response = client.get(url)

    assert response.status_code == 403

