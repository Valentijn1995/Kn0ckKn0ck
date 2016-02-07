from unittest import TestCase
from Parsing.ProxyExtractor import ProxyExtractor
from Parsing.Readers.CSVReader import CSVReader
from Proxies.HttpProxy import HttpProxy


class TestProxyExtractor(TestCase):

    def setUp(self):
        proxy_file_path = './Docs/Proxyfile_examples/local_proxy.csv'
        reader = CSVReader(proxy_file_path)
        self._extractor = ProxyExtractor(reader)

    def test_get_proxy(self):
        self.assertIsInstance(self._extractor.get_proxy(0), HttpProxy)

    def test_get_all_proxies(self):
        self.assertIsInstance(self._extractor.get_all_proxies()[0], HttpProxy)

    def test_get_count(self):
        self.assertEqual(self._extractor.get_proxy_count(), 1)

    def test_index_error(self):
        with self.assertRaises(IndexError):
            self._extractor.get_proxy(100)

    def tearDown(self):
        pass
