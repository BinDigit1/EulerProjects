import unittest
import digit_factorial

class DigitFactorialTest(unittest.TestCase):
    """Tests for `digit_factorials.py`."""

    def test_is_digit_factorial(self):
        """Is 145 successfully determined to be a curious digit factorial?"""
        self.assertTrue(digit_factorial.isDigitFactorial(145))
        self.assertFalse(digit_factorial.isDigitFactorial(146))

if __name__ == '__main__':
    unittest.main()