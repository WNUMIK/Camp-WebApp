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


# @pytest.mark.parametrize('email, fullname, password1, password2, status_code, number', (
#         ('tester@tester.pl', 'tester', 'ExamplePass', 'ExamplePass', 200, 1),
#         # ('', 'janusz', 'ExamplePass', 'ExamplePass', 200, 0),
#         # ('a', 'januszek', 'ExamplePass4', 'ExamplePass4', 200, 0),
#         # ('tester1', 'dodo', 'ExamplePass1', 'ExamplePass1', 200, 1),
#         # ('tester', 'diax', 'password', 'password', 200, 0),
#         # ('tester2', 'wow', 'ExamplePass1', 'ExamplePass', 200, 0),
#         # ('tester', 'Mirek', 'ExamplePass', 'ExamplePass2', 200, 0),
#         # ('tester4', 'Wow', '', 'ExamplePass2', 200, 0),
#         # ('tester4', 'Jasio', 'ExamplePass2', '', 200, 0),
#         # ('tester4', '', '', '', 200, 0),
#         ('', '', '', '', 200, 0),
# ))
# def test_registration_user2(db, client, email, fullname, password1, password2, status_code, number):
#     response = client.post(reverse('users:registration'), data={
#         'email': email,
#         'fullname': fullname,
#         'password1': password1,
#         'password2': password2,
#     })
#
#     assert response.status_code == status_code
#     assert get_user_model().objects.all().count() == number
