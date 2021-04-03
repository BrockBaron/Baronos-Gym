from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exclass import Class

import repositories.exclass_repository as exclass_repository

class_blueprint = Blueprint("classes", __name__)

@class_blueprint.route('/classes')
def classes():
    classes = exclass_repository.select_all()
    return render_template('classess/index.html', classes = classes)

#CREATE NEW CLASS

#UPDATED CLASS

#DELETE CLASS
