import unittest
from calculator import Calculate
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculate()

    def test_instantiate_calc(self):
        self.assertIsInstance(self.calculator, Calculate)

    def test_result_calc(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition_calc(self):
        td_add = CsvReader('Source/Addition.csv').data
        for row in td_add:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction_calc(self):
        td_sub = CsvReader('Source/Subtraction.csv').data
        for row in td_sub:
            self.assertNotEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertNotEqual(self.calculator.result, int(row['Result']))

    def test_multiplication_calc(self):
        td_mul = CsvReader('Source/Multiplication.csv').data
        for row in td_mul:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_calc(self):
        td_div = CsvReader('Source/Division.csv').data
        for row in td_div:
            self.assertNotEqual(self.calculator.divide(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertNotEqual(self.calculator.result, float(row['Result']))

    def test_square_calc(self):
        td_sq = CsvReader('Source/Square.csv').data
        for row in td_sq:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_root_calc(self):
        td_sqrt = CsvReader('Source/Square Root.csv').data
        for row in td_sqrt:
            self.assertEqual(self.calculator.square_root(float(row['Value 1'])), round(float(row['Result']), 7))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 7))


if __name__ == '__main__':
    unittest.main()
