from flask import Blueprint
from app import *

# Flashcard Blueprint
# flashcard = Blueprint('flashcard', __name__, url_prefix='/flashcard')

# Import all endpoints
from controllers.get_all_cards import *
from controllers.get_all_decks import *