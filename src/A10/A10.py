import unittest

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

class TestMathFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(5, -2), 3)

    def test_add_zero(self):
        self.assertEqual(add(10, 0), 10)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -2), -3)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(5, -2), 7)

    def test_subtract_zero(self):
        self.assertEqual(subtract(10, 0), 10)

if __name__ == '__main__':
    unittest.main()