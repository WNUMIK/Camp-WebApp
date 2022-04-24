import pytest
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse


def test_login_page(client):
    """
    Test login page for proper text
    """
    url = reverse('users:login')
    response = client.get(url)

    assert '<h1>Login</h1>' in response.content.decode('UTF-8')


def test_registration_user(db, client):
    """
    Test registration user
    """
    response = client.post(reverse('users:registration'), data={
        'fullname': 'Tester',
        'email': 'tester@pytest.pl',
        'password1': 'testPass',
        'password2': 'testPass',
    })

    assert response.status_code == 200
    assert get_user_model().objects.all().count() == 1


def test_login(user, client):
    """
    Test login user
    """
    assert client.login(email='a@a.pl', password='testPass123')


def test_login_user(user, client):
    """
    Test login user with post
    """
    response = client.post(reverse('users:login'), data={
        'username': user.email,
        'password': 'testPass123'
    })

    assert response.status_code == 302


def test_register_page(client):
    """
    Test status code of register page
    """
    url = reverse('users:registration')
    response = client.get(url)

    assert response.status_code == 200

