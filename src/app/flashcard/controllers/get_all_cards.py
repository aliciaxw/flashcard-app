from app.constants import *
from . import *

# @flashcard.route('/cards', methods=['GET', 'POST', 'DELETE'])
# def cards_crud():
#   return jsonify("Hello World!")

# class GetAllCardsController(AppDevController):
class GetAllCardsController(object):
  def get_path(self):
    return '/cards/'

  def get_methods(self):
    return ['GET']

  def content(self, **kwargs):
    cards = cards_dao.get_all_cards()
    serialized_cards = [card_schema.dump(cd).data for cd in cards]
    return serialized_cards