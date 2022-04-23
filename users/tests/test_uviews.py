from django.contrib.auth import get_user_model
from django.urls import reverse


def test_login_page(client):
    url = reverse('users:login')
    response = client.get(url)

    assert response.status_code == 200
    assert '<h1>Login</h1>' in response.content.decode('UTF-8')


def test_registration_user(db, client):
    response = client.post(reverse('users:registration'), data={
        'fullname': 'Pytest User',
        'email': 'tester@pytest.pl',
        'password1': 'testPass',
        'password2': 'testPass',

    })

    assert response.status_code == 200
    assert get_user_model().objects.all().count() == 1
