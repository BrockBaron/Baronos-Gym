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
member2 = Member('Andrew', 'Scott', 33, 'Male')
member_repository.save(member2)
member3 = Member('Callum', 'Mark', 33, 'Male')
member_repository.save(member3)
member4 = Member('Jamie', 'Kirk', 33, 'Male')
member_repository.save(member4)
member5 = Member('Marc', 'Johnston', 33, 'Male')
member_repository.save(member5)
member6 = Member('Euan', 'Orr', 34, 'Male')
member_repository.save(member6)
member7 = Member('Craig', 'Lauder', 34, 'Male')
member_repository.save(member7)
member8 = Member('Calum', "O'Keefe", 34, 'Male')
member_repository.save(member8)
member9 = Member('Rachel', 'Carr', 33, 'Female')
member_repository.save(member9)
member10 = Member('Suki', 'Trap', 33, 'Female')
member_repository.save(member10)


exclass1 = Exclass('Keen', 'Spinning', 90, 15)
exclass_repository.save(exclass1)
exclass2 = Exclass('Big', 'Weights', 60, 6)
exclass_repository.save(exclass2)
exclass3 = Exclass('Fast', 'Circuits', 60, 15)
exclass_repository.save(exclass3)
exclass4 = Exclass('High', 'Bounce', 60, 10)
exclass_repository.save(exclass4)
exclass5 = Exclass('Burning', 'Kettle Bells', 45, 10)
exclass_repository.save(exclass5)


booking1 = Booking(member1, exclass1)
booking_repository.save(booking1)
booking2 = Booking(member2, exclass2)
booking_repository.save(booking2)
booking3 = Booking(member3, exclass3)
booking_repository.save(booking3)
booking4 = Booking(member4, exclass4)
booking_repository.save(booking4)
booking5 = Booking(member5, exclass5)
booking_repository.save(booking5)

pdb.set_trace()
