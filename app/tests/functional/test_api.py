import pytest
from app import create_app


@pytest.fixture
def app():
    return create_app()


def test_list_all_items(app):
    with app.test_client() as test_client:
        response = test_client.get('/weather')
        print(response.data)
        assert 5 == len(response.get_json())


def test_list_all_items_with_max_param(app):
    with app.test_client() as test_client:
        response = test_client.get('/weather?max=2')
        assert 2 == len(response.get_json())


'''
    @todo Add fake database
'''
# def test_find_city_by_name(app):
#     with app.test_client() as test_client:
#         response = test_client.get('/weather/London')
#         assert 'London' == response.get_json().get('city')
#
#
# def test_not_found_city_in_api(app):
#     with app.test_client() as test_client:
#         response = test_client.get('/weather/teste')
#         assert '404' == response.get_json().get('cod')
#         assert 'city not found' == response.get_json().get('message')
