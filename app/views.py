import os
import requests
from flask import Blueprint, jsonify, current_app, request
from .cache import cache
from .serializer import HistoricSchema
from .model import Historic

bp_views = Blueprint('views', __name__)
api_key = os.getenv('API_KEY')
api_url = 'https://api.openweathermap.org/data/2.5/weather?units=metric&appid='+api_key


@bp_views.route('/weather', methods=['GET'])
def weather():
    max_items = request.args.get('max')
    default_items_quantity = '5'
    max_number = max_items if max_items else default_items_quantity

    hs = HistoricSchema(many=True)
    query = Historic.query.order_by(Historic.id.desc()).limit(max_number).all()
    print(hs.jsonify(query))

    return hs.jsonify(query)


@bp_views.route('/weather/<city_name>', methods=['GET'])
@cache.cached(timeout=30)
def weather_city(city_name: str):
    response = requests.get(api_url+'&q='+city_name).json()

    if response.get('cod') != 200:
        return jsonify(response), 404

    data = {
        'city': response.get('name'),
        'description': response.get('weather')[0].get('description'),
        'temperature': f'{round(response.get("main").get("temp"))}ºC'
    }

    hs = HistoricSchema()
    city = hs.load(data)

    current_app.db.session.add(city)
    current_app.db.session.commit()

    return hs.jsonify(city)


