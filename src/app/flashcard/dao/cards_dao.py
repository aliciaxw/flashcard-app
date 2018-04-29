from app.constants import *
from . import *

def get_card_by_id(card_id):
  return Card.query.filter(Card.id==card_id).first()

def get_card_by_front(front):
  return Card.query.filter(Card.front==front).first()

def get_all_cards():
  return Card.query.all()

def create_card(front, back, deck_id):
  # TODO: cards in the same deck should not have same frront
  card = Card(front=front, back=back, deck_id=deck_id)
  db_utils.commit_model(card)
  return card