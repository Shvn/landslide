from flask import Blueprint, render_template, redirect, url_for, request, jsonify, abort, Response, session
from landslide.model.data import Data

data_bp = Blueprint('data',__name__)

@data_bp.route('/')
def index():
    result = Data.find_all()
    return render_template('show-all-data.html', data=result)

@data_bp.route('/create')
def create():
    return render_template('create-data.html')

@data_bp.route('/<id>')
@data_bp.route('/<id>/show')
@data_bp.route('/<id>/edit')
def show(id):
    id_data = Data.find_by_id(id)
    if id_data == None:
        abort(404)
    else:
        return render_template('show-data.html', data=id_data)

@data_bp.route('/add', methods = ['post'])
def add():
    result = {}
    if 'action' not in request.form or request.form['action'] != 'add':
        result['status'] = 'error'
        result['status_msg'] = 'Action is not allowed'
        return redirect(url_for('data.create'), 302, result)
    #store data from post to db
    if request.form == None:
        result['status'] = 'error'
        result['status_msg'] = 'No data found'
    else:
        data = request.form
        id = Data.add(data)
        return redirect(url_for('.show', id=id))

@data_bp.route('/<id>/update', methods = ['post'])
def update(id):
    result = {}
    if 'action' not in request.form or request.form['action'] != 'update':
        result['error'] = True
        return redirect(url_for('.show', id=id), 302, result)
    #update data from post to db
    if request.form == None:
        result['status'] = 'error'
        result['status_msg'] = 'No data found'
    else:
        data = request.form
        Data.update(id, data)
        return redirect(url_for('.show', id=id))

@data_bp.route('/<id>/delete', methods = ['post'])
def delete(id):
    result = {}
    if 'action' not in request.form or request.form['action'] != 'delete':
        result['error'] = True
        return redirect(url_for('.show'), 302, result)
    #delete data from db
    if request.form == None:
        result['status'] = 'error'
        result['status_msg'] = 'No data found'
    else:
        Data.delete(id)
        return redirect(url_for('.index'))
