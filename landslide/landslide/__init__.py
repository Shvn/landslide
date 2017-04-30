'''
The flask application package.
'''

from flask import Flask
from flask_session import Session
app = Flask(__name__)

# Load the development configuration
app.config.from_object('config.development')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE', silent=True)

# session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

#import the views
from view.test import test_bp

#add the blueprints
app.register_blueprint(test_bp)
