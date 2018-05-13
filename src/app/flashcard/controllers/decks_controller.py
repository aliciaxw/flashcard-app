from app.constants import *
from . import *

from flask import json, jsonify, request

@flashcard.route('/decks', methods=['GET'])
def get_all_decks():
  decks = decks_dao.get_all_decks()
  op = decks_schema.dump(decks).data
  return jsonify({'decks': op})
  
# maybe not used
@flashcard.route('/decks/<int:deck_id>')
def get_deck_by_id(deck_id):
  deck = decks_dao.get_deck_by_id(deck_id)
  op = deck_schema.dump(deck).data
  return jsonify({'deck': op})

# @flashcard.route('/decks/<str:deck_name>')
# def get_deck_by_name(deck_name):
#   deck = decks_dao.get_deck_by_name(deck_name)
#   op = deck_schema.dump(deck).data
#   return jsonify({'deck': op})
  
@flashcard.route('/decks', methods=['POST'])
def create_deck():
  name = request.args.get('name')
  deck = decks_dao.create_deck(name=name)
  op = deck_schema.dump(deck).data
  return jsonify({'deck': op})
  
@flashcard.route('/decks', methods=['DELETE'])
def delete_deck():
  deck_id = request.args.get('id')
  return decks_dao.delete_deck_by_id(deck_id)

@flashcard.route('/decks', methods=['PATCH'])
def update_deck():
  # edit name of deck 
  # TODO
  pass