from app.constants import *
from . import *

# class GetAllDecksController(object):
#   def get_path(self):
#     return '/decks/'

#   def get_methods(self):
#     return ['GET']

#   def content(self, **kwargs):
#     decks = decks_dao.get_all_cards()
#     serialized_decks = [deck_schema.dump(dk).data for dk in decks]
#     return serialized_decks

@flashcard.route('/decks', methods=['GET'])
def get_all_decks():
  # TODO
  decks = decks_dao.get_all_decks()
  obs = decks_schema.dump(decks).data
  

@flashcard.route('/decks/<int:deck_id>')
def get_deck_by_id(deck_id):
  # TODO

@flashcard.route('/decks', methods=['POST'])
def create_deck():
  # TODO

@flashcard.route('/decks', methods=['DELETE'])
def delete_deck():
  # TODO

@flashcard.route('/decks', methods=['PATCH'])
def update_deck():
  # edit name of deck 
  # TODO