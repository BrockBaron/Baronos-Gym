import pdb
from re import M

from models.booking import Booking
from models.member import Member
from models.exclass import Exclass

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.exclass_repository as exclass_repository

booking_repository.delete_all()
member_repository.delete_all()
exclass_repository.delete_all()



member1 = Member('Max', 'Power', 40, 'Male')
member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)
# member1 = Member('Max', 'Power', 40, 'Male')
# member_repository.save(member1)

exclass1 = Exclass('Keen', 'Spinning', 90, 15)
exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)
# exclass1 = Exclass('Keen', 'Spinning', 90, 15)
# exclass_repository.save(exclass1)

booking1 = Booking(member1, exclass1)
booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)
# booking1 = Booking(member1, exclass1)
# booking_repository.save(booking1)











pdb.set_trace()
