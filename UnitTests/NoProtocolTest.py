from Proxies.Protocols.NoProtocol import NoProtocol
from unittest import TestCase


class TestNoProtocol(TestCase):

    def setUp(self):
        self.byte_string = b"Hello World!"
        self._no_prot = NoProtocol(self.byte_string)

    def test_get_bytes(self):
        self.assertEqual(self._no_prot.get_bytes(), self.byte_string)

    def test_to_str(self):
        my_string = str(self.byte_string)
        self.assertEqual(self._no_prot.__str__(), my_string)

    def tearDown(self):
        pass
