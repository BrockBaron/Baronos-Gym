import pdb

from models.booking import Booking
from models.member import Member
from models.exclass import Class

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.exclass_repository as exclass_repository

booking_repository.delete_all()
member_repository.delete_all()
exclass_repository.delete_all()



















pdb.set_trace()
