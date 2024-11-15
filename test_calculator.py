import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(9, 9), 18)
        self.assertEqual(self.calc.add(-9, 9), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-2, -5), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 9), 27)
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(12, 4), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()