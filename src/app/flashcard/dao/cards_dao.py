from app.constants import *
from . import *

def get_card_by_id(card_id):
  return Card.query.filter(Card.id==card_id).first()

def get_card_by_front(front):
  return Card.query.filter(Card.front==front).first()

def get_all_cards():
  return Card.query.all()

def create_card(front, back, card_id):
  card = Card(front=front, back=back, card_id=card_id)
  db.session.add(card)

  try:
    db.session.commit()
    return card 
  except Exception as e:
    db.session.rollback()
    return e

def delete_card_by_id(card_id):
  try:
    card = get_card_by_id(card_id)
    db.session.delete(card)
  except Exception:
    raise Exception('Something went wrong: Deletion')
  
  try:
    db.session.commit()
    return jsonify({"success": True})
  except Exception:
    db.session.rollback()
    raise Exception('Something went wrong: Commit to session')

def update_card(card_id):
  # TODO 