import unittest
import calculator


class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(calculator.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 3), 9)

    def test_divide(self):
        self.assertEqual(calculator.divide(15, 3), 5)


if __name__ == "__main__":
    unittest.main()
