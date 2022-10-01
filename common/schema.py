from marshmallow import fields
from flask_marshmallow import Marshmallow
ma = Marshmallow()

class ItemSchema(ma.Schema):
    id = fields.String(attribute='mal_id')