from app.constants import *
from . import *

class GetAllDecksController(object):
  def get_path(self):
    return '/decks/'

  def get_methods(self):
    return ['GET']

  def content(self, **kwargs):
    decks = decks_dao.get_all_cards()
    serialized_decks = [deck_schema.dump(dk).data for dk in decks]
    return serialized_decks