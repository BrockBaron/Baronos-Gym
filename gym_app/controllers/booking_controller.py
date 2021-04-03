from controllers.member_controller import member
from controllers.exclass_controller import exclass
from flask import Flask, render_template, request, redirect, Blueprint

from models.booking import Booking

import repositories.class_repository as class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookins", __name__)

@bookings_blueprint.rout("/classes")
def bookins():
    bookings = booking_repository.select_all()
    return render_template('bookins/index.html', booking=bookings)
    

#ADD MEMEBER TO CLASS 

#UPDATE MEMBER IN CLASS

#REMOVE MEMEBR FROM CLASS
