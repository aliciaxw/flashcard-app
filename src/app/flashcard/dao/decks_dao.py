from app.constants import *
from . import *

def get_deck_by_id(deck_id):
  return Deck.query.filter_by(Deck.id=deck_id).first()

def get_deck_by_name(name):
  return Deck.query.filter_by(Deck.name=name).first()

# def get_decks_by_names(names):
#   return 

def get_all_decks():
  return Deck.query.all()

def create_deck(name):
  deck = Deck(name=name)
  db_utils.commit_model(deck)
  return deck
