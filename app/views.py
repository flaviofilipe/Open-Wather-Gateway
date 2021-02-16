import os
import requests
from flask import Blueprint, jsonify, request, render_template, Response

bp_views = Blueprint('views', __name__)
api_key = os.getenv('API_KEY')
api_url = 'https://api.openweathermap.org/data/2.5/weather?units=metric&appid='+api_key


@bp_views.route('/weather', methods=['GET'])
def weather():
    max_items = request.args.get('max')
    default_items_quantity = '5'
    max_number = max_items if max_items else default_items_quantity

    response = {'param': max_number}

    return jsonify(response)


@bp_views.route('/weather/<city_name>', methods=['GET'])
def weather_city(city_name: str):
    response = requests.get(api_url+'&q='+city_name).json()

    if response.get('cod') != 200:
        return jsonify(response), 404

    data = {
        'city': response.get('name'),
        'description': response.get('weather')[0].get('description'),
        'temperature': f'{round(response.get("main").get("temp"))}ºC'
    }

    return jsonify(data)

