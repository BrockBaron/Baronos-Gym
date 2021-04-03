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
