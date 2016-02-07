from Proxies.DebugProxy import DebugProxy
from Proxies.Proxy import ProxyError
from Proxies.Protocols.NoProtocol import NoProtocol
from unittest import TestCase


class TestProxy(TestCase):

    def setUp(self):
        self._proxy = DebugProxy(False)

    def test_send_error(self):
        with self.assertRaises(ProxyError):
            self._proxy.send(NoProtocol(b"Hello World!"))

    def test_receive_error(self):
        with self.assertRaises(ProxyError):
            self._proxy.receive()
