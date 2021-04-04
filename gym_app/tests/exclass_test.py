import unittest
from models.exclass import Exclass, TestExclass

class TestExclass(unittest.TestCase):
    
    def setUp(self): Exclass('Power House', 'Weights', 45, 6)
    
    #1 excersise class has name 
    @unittest.skip("Delete this line to run the test")
    def test_exclass_has_name(self):
        self.assertEqual("Power House", self.exclass.name)
    
    #2 excersise class has activity type 
    @unittest.skip("Delete this line to run the test")
    def test_exclass_has_activity_type(self):
        self.assertEqual("Weights", self.exclass.activity_type)
        
    #3 excersise class has duration 
    @unittest.skip("Delete this line to run the test")
    def test_exclass_has_duration(self):
        self.assertEqual("45", self.exclass.duration)
        
    #4 excersise class has capacity value 
    @unittest.skip("Delete this line to run the test")
    def test_exclass_has_capacity_value(self):
        self.assertEqual("6", self.exclass.capacity)
        
    
        