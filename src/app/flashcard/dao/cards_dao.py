from app.constants import *
from . import *

def get_card_by_id(card_id):
  return Card.query.filter_by(Card.id=card_id).first()

def get_card_by_front(front):
  return Card.query.filter_by(Card.front=front).first()

def get_all_cards():
  return Card.query.all()

def create_card(front, back='', deck_id):
  card = Card(front=front,back=back,deck_id=deck_id)

  # do not allow cards with same front in the same deck
  same_front = Card.query.filter_by(Card.front=front, Card.deck_id=deck_id).first()
  if same_front is None:
    db_utils.commit_model(card)
    return card