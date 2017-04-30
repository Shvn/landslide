"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from landslide import app
import urllib2
import json


import models

@app.route('/')
@app.route('/home')
def home():
    return "hello"
