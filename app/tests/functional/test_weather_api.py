import os
import pytest
import requests


@pytest.fixture
def get_api_token():
    return os.getenv('API_KEY')


@pytest.fixture
def get_api_url():
    return 'https://api.openweathermap.org/data/2.5/weather'


def test_if_token_exists(get_api_token):
    assert get_api_token is not None


def test_find_london_city_in_weather_api(get_api_url, get_api_token):
    find_city = '{}?appid={}&q=London'.format(get_api_url, get_api_token)
    response = requests.get(find_city)
    assert response.status_code == 200
    assert 200 == response.json().get('cod')
    assert 'London' == response.json().get('name')


def test_not_found_city_in_weather_api(get_api_url, get_api_token):
    find_city = '{}?appid={}&q=Teste'.format(get_api_url, get_api_token)
    response = requests.get(find_city)
    assert response.status_code == 404
    assert 'city not found' == response.json().get('message')


def test_not_found_city_in_weather_api(get_api_url, get_api_token):
    find_city = '{}?appid={}&q=Teste'.format(get_api_url, get_api_token)
    response = requests.get(find_city)
    assert 'city not found' == response.json().get('message')
