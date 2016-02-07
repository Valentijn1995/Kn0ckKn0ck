from Parsing.Readers.CSVReader import CSVReader
from unittest import TestCase


class TestCSVReader(TestCase):

    def setUp(self):
        proxy_file_path = './Docs/Proxyfile_examples/example.csv'
        self._reader = CSVReader(proxy_file_path)

    def test_get_value(self):
        self.assertEquals(self._reader.get_value('Port', 1), '8000')
        self.assertEquals(self._reader.get_value(6, 1), 'Admin')
        self.assertEquals(self._reader.get_value(6, 0), '')

    def test_get_item(self):
        self.assertEquals(self._reader.get_item(1), {'Proxy name': 'My second proxy', 'Address': '192.168.1.2',
                                                     'Port': '8000', 'Type': 'http-proxy', 'Auth method': 'basic',
                                                     'Username': 'Admin', 'Password': 'Admin'})
        self.assertEquals(self._reader.get_item(0), {'Proxy name': 'My first proxy', 'Address': '192.168.1.1',
                                                     'Port': '8080', 'Type': 'http-proxy', 'Auth method': 'none',
                                                     'Username': '', 'Password': ''})

    def test_get_count(self):
        self.assertEquals(self._reader.get_count(), 3)

    def test_value_exists(self):
        self.assertTrue(self._reader.value_exists("Proxy name"))
        self.assertFalse(self._reader.value_exists("Non existing property"))

    def test_bad_column_error(self):
        bad_column_path = './Docs/Proxyfile_examples/bad_column_example.csv'

        with self.assertRaises(ValueError):
            reader = CSVReader(bad_column_path)
            reader.get_value('Address', 0)

    def test_bad_row_error(self):
        bad_row_path = './Docs/Proxyfile_examples/bad_row_example.csv'

        with self.assertRaises(ValueError):
            CSVReader(bad_row_path)

    def tearDown(self):
        pass
