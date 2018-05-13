from app.constants import *
from . import *

# @flashcard.route('/cards', methods=['GET', 'POST', 'DELETE'])
# def cards_crud():
#   return jsonify("Hello World!")

@flashcard.route('/cards', methods = ['POST'])
def create_card():
  front = request.args.get('front')
  back = request.args.get('back')
  deck_id = request.args.get('deck_id')
  card = cards_dao.create_card(
           front=front,
           back=back,
           deck_id=deck_id)
  op = card_schema.dump(card).data
  return jsonify({'card': op})

@flashcard.route('/cards', methods = ['DELETE'])
def delete_card():
  card_id = request.args.get('card_id')
  return cards_dao.delete_card_by_id(card_id)

@flashcard.route('/cards', methods = ['PATCH'])
def update_card():
  # update front, back, or what deck it's in 
  # TODO
  pass