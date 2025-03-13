import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../src'))

from question_a.question_a import is_prime

from question_c.question_c import use_local_variable
from question_b.question_b import reverse_string
from question_d.question_d import get_assessment_value,get_tax_assessed
# Test cases for is_prime
class TestQuestionA(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)   # 2 is a prime number
        self.assertEqual(is_prime(4), False)  # 4 is not a prime number
        self.assertEqual(is_prime(17), True)  # 17 is a prime number
        self.assertEqual(is_prime(1), False)  # 1 is not a prime number
        self.assertEqual(is_prime(0), False)  # 0 is not a prime number

# Test cases for use_local_variable
class TestQuestionC(unittest.TestCase):
    def test_local_variable_behavior(self):
        original_num = 50
        modified_num = use_local_variable(original_num)
        self.assertEqual(original_num, 50)  # Ensure the original number is unchanged
        #self.assertEqual(modified_num, 100)  # Ensure the returned number is modified
class TestQuestionB(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
class TestPropertyTaxCalculator(unittest.TestCase):
    def test_get_assessment_value(self):
        self.assertEqual(get_assessment_value(10000), 6000)
        self.assertEqual(get_assessment_value(20000), 12000)
    
    def test_get_tax_assessed(self):
        self.assertAlmostEqual(get_tax_assessed(6000), 43.20, places=2)
        self.assertAlmostEqual(get_tax_assessed(10000), 72.00, places=2)
   
if __name__ == "__main__":
    unittest.main()


