'''
The flask application package.
'''

from flask import Flask, Blueprint
from flask_session import Session
from jinja2 import Environment
from werkzeug.utils import secure_filename
app = Flask(__name__)


import landslide.views

# Load the development configuration
app.config.from_object('config.development')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE', silent=True)

# session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
