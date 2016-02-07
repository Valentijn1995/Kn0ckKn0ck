from Proxies.Protocols.NoProtocol import NoProtocol
from Proxy import Proxy


class NoProxy(Proxy):
    """
        A proxy which is actually no proxy? That's right! The NoProxy class extends from the Proxy class but is
        actually no proxy but a direct connection. It's used when the program does not make use of a proxy.
        This method makes the implementation of AttackMethods easier by 'abstracting' away the connection.

        This approach prevents if-else like connection structures like the following one:

        if isinstance(myProxy, Proxy):
            myProxy.send(myProtocol)
        elif isinstance(myProxy, socket)
            myProxy.send(myProtocol.get_bytes())

        Not all methods are documented because they are already documented in the Proxy class.
    """

    def __init__(self):
        """
            Constructor. No proxy address needed because this class is not actually a proxy
        """
        super(NoProxy, self).__init__(None)
        self._proxy_socket = None

    def _connect(self, destination):
        self._proxy_socket = self._init_connection(destination.address, destination.port)

    def is_connected(self):
        return self._proxy_socket is not None

    def _send(self, payload):
        self._proxy_socket.send(payload.get_bytes())

    def _receive(self):
        received_bytes = self._read_until_empty(self._proxy_socket)
        return NoProtocol(received_bytes)

    def _close(self):
        self._proxy_socket.close()
        self._proxy_socket = None

    def copy(self):
        return NoProxy()
