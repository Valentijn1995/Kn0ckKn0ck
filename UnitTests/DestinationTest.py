from Proxies.Destination import Destination
from unittest import TestCase


class TestDestination(TestCase):

    def setUp(self):
        self._test_dest = Destination("192.168.1.1", 81)

    def test_address(self):
        self.assertEquals(self._test_dest.address, "192.168.1.1")

    def test_port(self):
        self.assertEquals(self._test_dest.port, 81)

    def test_port_error(self):
        with self.assertRaises(ValueError):
            Destination('127.0.0.1', 'Fake port')

    def tearDown(self):
        pass
