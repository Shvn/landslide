"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from landslide import app
import urllib2
import json


@app.route('/')
@app.route('/home')
def home():
    return "hello"

@app.route('/view-map')
def viewmap():
    req = urllib2.Request("https://data.nasa.gov/resource/tfkf-kniw.json")
    opener = urllib2.build_opener()
    f = opener.open(req)
    jso = json.loads(f.read())
    return jso
