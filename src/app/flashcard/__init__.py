from flask import Blueprint
from app import *

# Flashcard Blueprint
flashcard = Blueprint('flashcard', __name__, url_prefix='/flashcard')

# Import all endpoints
from controllers.decks_controller import *
from controllers.cards_controller import *