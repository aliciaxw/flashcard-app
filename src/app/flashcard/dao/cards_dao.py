from app.constants import *
from . import *

"""
Add more methods below!!!
"""

def card_by_id(card_id):
  """
  Get board by ID
  """
  return Card.query.filter_by(id=board_id).first()

def card_by_front()