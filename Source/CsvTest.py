import unittest
from CsvReader import CsvReader, ClassFactory


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Source/Addition.csv')

    def test_return_data(self):
        values = self.csv_reader.return_data('Value')
        self.assertIsInstance(values, list)
        test_class = ClassFactory('Value', self.csv_reader.data[0])
        for value in values:
            self.assertEqual(value.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()
