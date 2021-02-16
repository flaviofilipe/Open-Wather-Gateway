from flask import Flask
from flask_cors import CORS, cross_origin

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    cors = CORS(app)
    
    from app.views import bp_views
    app.register_blueprint(bp_views)

    return app
