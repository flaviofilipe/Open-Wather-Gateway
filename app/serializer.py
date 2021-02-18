from marshmallow import fields
from flask_marshmallow import Marshmallow
from app.model import Historic

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class HistoricSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Historic
        load_instance = True

    city = fields.Str(required=True)
    description = fields.Str(required=True)
    temperature = fields.Str(required=True)
