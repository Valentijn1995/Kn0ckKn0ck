from unittest import TestCase
from Parsing.Readers.Table import Table


class TestTable(TestCase):
    """
        Test case for testing the different methods of the Table class
    """

    def setUp(self):
        header = ['Animal', 'Name']
        table = [['Dolphin', 'Joe'], ['Cat', 'Max'], ['Dog', 'John'], ['Hamster', 'Jenny']]
        self._test_table = Table(header, table)

    def test_get_cell(self):
        self.assertEquals(self._test_table.get_cell('Name', 1), 'Max')

    def test_get_column(self):
        self.assertEquals(self._test_table.get_column('Animal'), ['Dolphin', 'Cat', 'Dog', 'Hamster'])

    def test_get_row(self):
        self.assertEquals(self._test_table.get_row(2), ['Dog', 'John'])

    def test_get_row_count(self):
        self.assertEquals(self._test_table.get_row_count(), 4)

    def test_row_error(self):
        with self.assertRaises(ValueError):
            header = ['Animal', 'Name']
            table = [['Dolphin', 'Joe'], ['Cat', 'Max'], ['Dog', 'John'], ['Hamster']]
            Table(header, table)

    def tearDown(self):
        pass
