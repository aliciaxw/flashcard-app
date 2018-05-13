from . import *

class Deck(Base):
  __tablename__ = 'decks'
  id             = db.Column(db.Integer, primary_key=True)
  name           = db.Column(db.String(255), unique=True, nullable=False)
  # cards          = db.relationship('Card', backref='decks')

  def __init__(self, **kwargs):
    self.name = kwargs.get('name')
