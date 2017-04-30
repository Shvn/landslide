from flask import Blueprint, render_template, redirect, url_for, request, jsonify, abort, Response, session

test_bp = Blueprint('test',__name__)

@test_bp.route('/')
def home():
    return "hello"
