from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint('members',__name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

#NEW 
#GET '/members/new'
@members_blueprint.route('/members/new', methods=['GET'])
def new_member():
    members = member_repository.select_all()
    return render_template("members/new.html", all_members = members)

#CREATE 
#POST '/members'

# SHOW 
#/members/<id>/ 
@members_blueprint.route("/members/<id>")
def show_member(id):
    member = member_repository.select(id)
    return render_template("members/show.html", member = member)


#EDIT
# GET '/members/<id>/edit'

#UPDATED
# PUT '/members/<id>'

#DELETE 
# DELETE '/members/<id>'