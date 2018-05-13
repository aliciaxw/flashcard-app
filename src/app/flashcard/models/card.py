from . import *

class Card(Base):
  __tablename__ = 'cards'
  id             = db.Column(db.Integer, primary_key=True)
  front          = db.Column(db.String(255), unique=True, nullable=False)
  back           = db.Column(db.Text(), unique=True, nullable=False)
  deck_id        = db.Column(db.Integer, db.ForeignKey('decks.id'), nullable=False)
  deck           = db.relationship('Deck', uselist=False, backref='cards')

  def __init__(self, **kwargs):
    self.front = kwargs.get('front')
    self.back = kwargs.get('back')
    self.deck_id = kwargs.get('deck_id')