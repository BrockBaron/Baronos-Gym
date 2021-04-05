from flask import Flask, render_template, request, redirect, Blueprint

from models.booking import Booking

import repositories.exclass_repository as exclass_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def booking():
    bookings = booking_repository.select_all()
    return render_template('bookings/index.html', bookings = bookings)

#NEW 
#GET '/bookings/new'
@bookings_blueprint.route('/bookings/new', methods=['GET'])
def new_booking():
    bookings = booking_repository.select_all()
    return render_template('bookings/new.html', all_bookings=bookings)


#CREATE 
#POST '/bookings'
@bookings_blueprint.route('/bookings', methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    exclass_id = request.form['exclass_id']
    member = member_repository.select(member_id)
    exclass = exclass_repository.select(exclass_id)
    booking = Booking(member, exclass)
    booking_repository.save(booking)
    return redirect('/bookings')
    
    
# SHOW 
#/bookings/<id>/ 
@bookings_blueprint.route('/bookings/<id>')
def show_booking(id):
    booking = booking_repository.select(id)
    return render_template('bookings/show.html', booking=booking)


# SHOW - member in particular class - need an alternative route? '/bookings/<id>/exclass'?
@bookings_blueprint.route('/bookings/<id>')
def show_members_in_exclass(id):
    exclass = exclass_repository.select(id)
    members = member_repository.get_by_exclass(exclass)
    return render_template('bookings/show.html', exclass = exclass, members = members)


#EDIT
# GET '/bookings/<id>/edit'
@bookings_blueprint.route('/bookings/<id>/edit', methods = ['GET'])
def edit_booking(id):
    exclass = exclass_repository.select(id)
    members = member_repository.select_all()
    return redirect('/bookings/edit.html', exclass = exclass, members = members)
    


#UPDATED
# PUT '/bookings/<id>'
@bookings_blueprint.route('/bookings/<id>', methods=['POST'])
def update_booking(id):
    member_id = request.form['member_id']
    exclass_id = request.form['exclass_id']
    member = member_repository.select(member_id)
    exclass = exclass_repository.select(exclass_id)
    booking = Booking(member, exclass, id)
    booking_repository.update(booking)
    return redirect('/bookings')




#DELETE 
# DELETE '/bookings/<id>'
@bookings_blueprint.route('/bookins/<id>/delete', methods = ['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect('/bookins')