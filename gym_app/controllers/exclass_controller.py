from controllers.member_controller import member
from flask import Flask, render_template, request, redirect, Blueprint

from models.exclass import Class

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
    members = member_repository.get_by_class(exclass)
    return render_template('classes//show.html', exclass = exclass, members = members)

#GET CLASSESS 

#CREATE NEW CLASS

#UPDATED CLASS

#DELETE CLASS
