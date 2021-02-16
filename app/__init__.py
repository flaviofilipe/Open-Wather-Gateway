from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    from app.views import bp_views
    app.register_blueprint(bp_views)

    return app
