from card import *
from deck import *

from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

# Using marshmallow-sqlalchemy will make your life a lot easier
#   Do some research into this!!
class CardSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = Card
    exclude = ('created_at', 'updated_at')

class DeckSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = Deck
    # ???
    exclude = ('created_at', 'updated_at')

# Serializers
card_schema = CardSchema()
deck_schema = DeckSchema()