import sys
import unittest
from main import Calculator


class TestCalculator(unittest.TestCase):
    var = 0
    def setUp(self):
        self.calculator = Calculator()

    @unittest.skip('Skip this test')
    def test_nothing(self):
        self.fail('Should not pass')

    @unittest.skipIf(var==0, 'not supported')
    def test_var(self):
        pass

    @unittest.skipUnless(sys.platform.startswith('win'), 'Windows only')
    def test_windows_support(self):
        pass

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(4, 6), 24)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_second(self):
        assert self.calculator.divide(10, 2) == 5, 'Не вірно, має бути 5'

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as err:
            self.calculator.divide(10, 0)
        assert str(err.exception) == 'Ділення на нуль неможливе'


if __name__ == '__main__':
    unittest.main()