import re
from db.run_sql import run_sql
from models.booking import Booking

import repositories.exclass_repository as exclass_repository
import repositories.member_repository as member_repository

# save new bookings, generate uniques booking number / id
def save(booking):
    sql = "INSER INTO bookings (member_id, exclass_id) VALUES (%s, %s, %s) RETURNING id"
    values = [booking.member.id, booking.exclass.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking


# select all bookings
def select_all():
    bookings = []
    
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    
    for row in results:
        member = member_repository.select(row['member_id'])
        exclass = exclass_repository.select(row['exclass_id'])
        booking = Booking(member, exclass, row['id'])
        bookings.append(booking)
    return booking

    
# delete all bookings

# delete individual booking by id

# ??show all members booked on specific class?? take/replace code from member repo 





