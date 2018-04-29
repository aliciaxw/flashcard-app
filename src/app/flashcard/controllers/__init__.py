from flask import request, render_template, jsonify
from functools import wraps # for decorators
import app

# Models
from app.flashcard.models.all import *

# DAO
from app.flashcard.dao import cards_dao, decks_dao

# Serializers
card_schema = CardSchema()
deck_schema = DeckSchema()

# Blueprint
# from app.flashcard import flashcard