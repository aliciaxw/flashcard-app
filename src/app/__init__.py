from flask import Blueprint, Flask, render_template, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from constants import *
import os

from app.flashcard import flashcard as flashcard

# Configure Flask app
app = Flask(__name__, static_url_path='/static')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Database
db = SQLAlchemy(app)

# Import + Register Blueprints
# Workflow is as follows:

app.register_blueprint(flashcard)

# Default functionality of rendering index.html
def render_page():
  return render_template('index.html')

from app.controllers.all import controllers as controllers
for controller in controllers:
  blueprint.add_url_rule(
    controller.get_path(),
    controller.get_name(),
    controller.response,
    methods=controller.get_methods()
  )

# React Catch All Paths
# @app.route('/', methods=['GET'])
# def index():
#   return render_page()
# @app.route('/<path:path>', methods=['GET'])
# def any_root_path(path):
#   return render_page()

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404
