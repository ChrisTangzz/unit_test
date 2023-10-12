import unittest
from HW1.my_module import hw1

class TestAddFunction(unittest.TestCase):
    def test_1(self):
        result = hw1.test1(1)
        expected_result = "大於0等於0大於0" 
        self.assertEqual(result, expected_result) 
    def test_2(self):
        result = hw1.test1(2)
        expected_result = "大於0大於0等於0"  
        self.assertEqual(result, expected_result)
    def test_neg_1(self):
        result = hw1.test1(-1)
        expected_result = "小於0等於0大於0"
        self.assertEqual(result, expected_result)
        
if __name__ == "__main__":
    unittest.main()