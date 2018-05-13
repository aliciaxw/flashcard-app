from card import *
from deck import *
from marshmallow_sqlalchemy import ModelSchema

# Using marshmallow-sqlalchemy will make your life a lot easier
#   Do some research into this!!
class CardSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = Card

class DeckSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = Deck

# Serializers
card_schema = CardSchema()
deck_schema = DeckSchema()