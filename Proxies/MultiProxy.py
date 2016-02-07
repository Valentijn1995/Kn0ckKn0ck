from Proxy import Proxy


class MultiProxy(Proxy):
    """
        Proxy which is composed of multiple proxy's. Another proxy will be used as soon as you call de connect method.
        This class makes use of the Composite design pattern. You can use the MultiProxy class as if it is one proxy
        but you are actually using multiple proxies.
    """
    def __init__(self, proxy_list):
        Proxy.__init__(self, None)
        self._current_proxy = None
        self._proxy_list = proxy_list
        self._proxy_counter = 0
        self._last_proxy_index = len(proxy_list)

    def _get_next_proxy(self):
        if self._proxy_counter >= self._last_proxy_index:
            self._proxy_counter = 0
        next_proxy = self._proxy_list[self._proxy_counter]
        self._proxy_counter += 1
        return next_proxy

    def _receive(self):
        return self._current_proxy.receive()

    def copy(self):
        return MultiProxy(self._proxy_list)

    def _connect(self, destination):
        self._current_proxy = self._get_next_proxy()
        self._current_proxy.connect(destination)

    def is_connected(self):
        return self._current_proxy is not None

    def _send(self, payload):
        self._current_proxy.send(payload)

    def _close(self):
        self._current_proxy.close()
        self._current_proxy = None
