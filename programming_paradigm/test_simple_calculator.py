import unittest
from simple_calculator import SimpleCalculator  # Import the SimpleCalculator class

class TestSimpleCalculator(unittest.TestCase):
    """Test case for the SimpleCalculator class"""

    def setUp(self):
        """This method will run before each test."""
        self.calc = SimpleCalculator()  # Create an instance of the calculator (now using 'calc')

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Test addition 2 + 3
        self.assertEqual(self.calc.add(-1, 1), 0)  # Test addition -1 + 1
        self.assertEqual(self.calc.add(-1, -1), -2)  # Test addition -1 + -1

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Test subtraction 5 - 3
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Test subtraction 3 - 5
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Test subtraction 0 - 0

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 3), 12)  # Test multiplication 4 * 3
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Test multiplication 0 * 5
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Test multiplication -2 * 3

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 2), 3)  # Test division 6 / 2
        self.assertEqual(self.calc.divide(5, 0), None)  # Test division by zero, expecting None
        self.assertEqual(self.calc.divide(-6, 2), -3)  # Test division -6 / 2

if __name__ == "__main__":
    unittest.main()
