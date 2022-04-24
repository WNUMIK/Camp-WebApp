import pytest
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse


def test_login_page(client):
    url = reverse('users:login')
    response = client.get(url)

    assert response.status_code == 200
    assert '<h1>Login</h1>' in response.content.decode('UTF-8')


def test_registration_user(db, client):
    response = client.post(reverse('users:registration'), data={
        'fullname': 'Tester',
        'email': 'tester@pytest.pl',
        'password1': 'testPass',
        'password2': 'testPass',
    })

    assert response.status_code == 302
    assert get_user_model().objects.all().count() == 1


def test_login(user, client):
    assert client.login(email='a@a.pl', password='testPass123')
