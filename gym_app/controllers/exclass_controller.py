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

# SHOW CLASSES
@exclass_blueprint.route('/classes/<id>')
def show(id):
    exclass = exclass_repository.select(id)
    return render_template('classes/show.html', exclass = exclass)

#NEW GET CLASSESS 
@exclass_blueprint.route('/classes/new', methods=['GET'])
def new_task():
    exclasses = exclass_repository.select_all()
    return render_template('classes/new.html', all_classes = exclasses)



#CREATE POST CLASSES


#UPDATED CLASS

#DELETE CLASS

#DELETE ALL CLASSESS
