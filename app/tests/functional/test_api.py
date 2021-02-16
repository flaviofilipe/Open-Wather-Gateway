import pytest
from app import create_app


@pytest.fixture
def app():
    return create_app();


def test_list_all_items(app):
    with app.test_client() as test_client:
        response = test_client.get('/weather')
        print(response.data)
        assert b'"param":"5"' in response.data


def test_list_all_items_with_max_param(app):
    with app.test_client() as test_client:
        response = test_client.get('/weather?max=10')
        assert '10' == response.get_json().get('param')


def test_find_city_by_name(app):
    with app.test_client() as test_client:
        response = test_client.get('/weather/London')
        assert 'London' == response.get_json().get('param')
