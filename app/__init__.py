from flask import Flask
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from app.cache import cache

from .model import configure as config_db
from .serializer import configure as config_ma


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.config['CACHE_TYPE'] = 'simple'


    cors = CORS(app)

    config_db(app)
    config_ma(app)
    cache.init_app(app)

    Migrate(app, app.db)

    from app.views import bp_views
    app.register_blueprint(bp_views)

    return app
