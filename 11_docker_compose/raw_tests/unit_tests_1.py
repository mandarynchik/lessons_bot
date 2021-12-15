"""
assert 2 + 2 == 4
assert 2 + 2 == 5, "Something went wrong"
assert(2 + 2 == 5, "Something went wrong")
"""

import unittest

class TestStringMethods(unittest.TestCase):
    """
    def test_numbers_equal_wrong(self):
        self.assertEqual(42, 24)
    
    def test_numbers_equal(self):
        self.assertEqual(42, 42)
    
    def check_numbers_equal(self):
        self.assertEqual(42, 24)
    """
    
    def test_show_asserts(self):
        self.assertTrue(isinstance(5, int))
        self.assertFalse(isinstance("5", int))
        self.assertFalse(isinstance(5, int))

        #self.assertEqual("Hello", "Hello")
        #self.assertEqual("Hello", "hell")
    

unittest.main()