"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from landslide import app

@app.route('/')
@app.route('/home')
def home():
    return "hello"
