from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Historic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    description = db.Column(db.String(255))
    temperature = db.Column(db.String(255))
