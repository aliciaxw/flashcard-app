from app.constants import *
from . import *

from flask import jsonify

def get_deck_by_id(deck_id):
  return Deck.query.filter(Deck.id==deck_id).first()

def get_deck_by_name(name):
  return Deck.query.filter(Deck.name==name).first()

def get_all_decks():
  return Deck.query.all()

def create_deck(name):
  if get_deck_by_name(name) != {}: # ?? 
    raise Exception('Deck with that name already exists')
  deck = Deck(name=name)
  db.session.add(deck)

  try:
    db.session.commit()
    return deck 
  except Exception as e:
    db.session.rollback()
    return e

def delete_deck_by_id(deck_id): 
  try:
    deck = get_deck_by_id(deck_id)
    db.session.delete(deck)
  except Exception:
    raise Exception('Something went wrong: Deletion')
    
  try:
    db.session.commit()
    return jsonify({"success":True})
  except Exception:
    db.session.rollback()
    raise Exception('Something went wrong: Commit to session')

def update_deck(deck_id):
  # TODO
  pass