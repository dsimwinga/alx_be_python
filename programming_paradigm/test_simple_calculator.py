import unittest
from simple_calculator import SimpleCalculator  # Import the SimpleCalculator class

class TestSimpleCalculator(unittest.TestCase):
    """Test case for the SimpleCalculator class"""

    def setUp(self):
        """This method will run before each test."""
        self.calculator = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(3, 5), -2)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calculator.multiply(4, 3), 12)
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.divide(5, 0), None)  # Check division by zero
        self.assertEqual(self.calculator.divide(-6, 2), -3)

if __name__ == "__main__":
    unittest.main()
