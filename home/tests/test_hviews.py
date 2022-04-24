from django.urls import reverse


def test_home_view(db, client):
    """
    Test status code of homepage
    """
    url = reverse('home:home')
    response = client.get(url)

    assert response.status_code == 200


def test_home_view2(db, client):
    """
    Test proper content display on homepage
    """
    url = reverse('home:home')
    response = client.get(url)
    assert 'Welcome!' in response.content.decode('UTF-8')
