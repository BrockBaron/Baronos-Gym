from controllers.member_controller import member
from flask import Flask, render_template, request, redirect, Blueprint

from models.exclass import Exclass

import repositories.exclass_repository as exclass_repository
import repositories.member_repository as member_repository

exclass_blueprint = Blueprint("classes", __name__)

@exclass_blueprint.route('/classes')
def classes():
    classes = exclass_repository.select_all()
    return render_template('classess/index.html', classes = classes)


#NEW 
#GET '/classes/new' 
@exclass_blueprint.route('/classes/new', methods=['GET'])
def new_task():
    exclasses = exclass_repository.select_all()
    return render_template('classes/new.html', all_classes = exclasses)


#CREATE 
#POST '/classes' - possibly need to route to a create path for pop-up from etc. '/classes/create'
@exclass_blueprint.route('/classes', methods=['POST'])
def create_exclass():
    name = request.form['name']
    activity_type = request.form['activity_type']
    duration = request.form['duration']
    capacity = request.form['capacity']
    exclass = Exclass(name, activity_type, duration, capacity)
    exclass_repository.save(exclass)
    return redirect('/classes') # possible rediretect to differnt location

# SHOW 
#'/classes/<id>/  - possible GET method needed
@exclass_blueprint.route('/classes/<id>')
def show_exclass(id):
    exclass = exclass_repository.select(id)
    return render_template('classes/show.html', exclass = exclass)

#EDIT
# GET '/classes/<id>/edit'
@exclass_blueprint.route('/classes/<id>/edit', methods=['GET'])
def edit_exclass(id):
    exclass = exclass_repository.select(id)
    return render_template('classes/edit.html', exclass = exclass)


#UPDATED
# PUT '/classes/<id>'
@exclass_blueprint.route('/classes/<id>', methods=['POST'])
def update_exclass(id):
    name = request.form['name']
    activity_type = request.form['activity_type']
    duration = request.form['duration']
    capacity = request.form['capacity']
    exclass = Exclass(name, activity_type, duration, capacity, id)
    exclass_repository.update(exclass)
    return render_template('/classes')

#DELETE 
# DELETE '/classes/<id>'
@exclass_blueprint.route('/classes/<id>/delete', methods=['POST'])
def delete_exclass(id):
    exclass_repository.delete(id)
    return redirect('/classes')



