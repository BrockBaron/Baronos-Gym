from controllers.member_controller import members

from flask import Flask, render_template, request, redirect, Blueprint

from models.exclass import Class

import repositories.member_repository as member_repository
import repositories.exclass_repository as exclass_repository

exclass_blueprint = Blueprint('/classes', __name__)

@exclass_blueprint.route("/classes")
def exclass():
    classes = exclass_repository.select_all()
    return render_template('classes/index.html', classes=classes)