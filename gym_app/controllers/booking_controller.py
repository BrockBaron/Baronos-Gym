from flask import Flask, render_template, request, redirect, Blueprint

from models.booking import Booking

import repositories.exclass_repository as exclass_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookins():
    bookings = booking_repository.select_all()
    return render_template('bookings/index.html', bookings = bookings)


#GET BOOKINGS

#ADD/CREATE NEW BOOKING ADD MEMEBER TO CLASS 

#DELETE BOOKINGS BY ID

#UPDATE MEMBER IN CLASS

#REMOVE MEMEBR FROM CLASS

#NEW 
#GET '/bookings/new'

#CREATE 
#POST '/bookings'

# SHOW 
#/bookings/<id>/ 
@bookings_blueprint.route('/bookings/<id>')
def show_booking(id):
    booking =booking_repository.select(id)
    return render_template('bookings/show.html', booking=booking)


# SHOW - member in particular class - need an alternative route?
@bookings_blueprint.route('/bookings/<id>')
def show_members_in_exclass(id):
    exclass = exclass_repository.select(id)
    members = member_repository.get_by_exclass(exclass)
    return render_template('bookings/show.html', exclass = exclass, members = members)


#EDIT
# GET '/bookings/<id>/edit'

#UPDATED
# PUT '/bookins/<id>'

#DELETE 
# DELETE '/bookins/<id>'
