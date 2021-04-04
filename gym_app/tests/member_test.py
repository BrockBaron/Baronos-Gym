import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    
    def setUp(self):
        self.member = Member('Max', 'Power', 40, 'Male')
        
    #1 member has name first
    @unittest.skip("Delete this line to run the test")
    def test_member_has_first_name(self):
        self.assertEqual("Max", self.memebr.first_name)
    
    #2 member has name second name
    @unittest.skip("Delete this line to run the test")
    def test_member_has_second_name(self):
        self.assertEqual("Power", self.memebr.second_name)
        
    #3 member has name age
    @unittest.skip("Delete this line to run the test")
    def test_member_has_age(self):
        self.assertEqual(40, self.memebr.age)
    
    #4 member has name second name
    @unittest.skip("Delete this line to run the test")
    def test_member_has_sex(self):
        self.assertEqual("Male", self.memebr.sex)