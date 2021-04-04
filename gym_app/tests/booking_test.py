import unittest
from models.booking import Booking

class TestBooking(unittest.TestCase):
    
    def setUp(self):
        self.booking = Booking("Max Power", "Big Lift")


#1 booking has name 
@unittest.skip("Delete this line to run the test")      
def test_booking_has_members(self):
    self.assertEqual("Max Power", self.booking.name)
        
#2 booking has exclasses
@unittest.skip("Delete this line to run the test")
def test_booking_has_exclasses(self):
    self.assertEqual("Big Lift", self.booking.exclass)
    
