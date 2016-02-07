class Destination:
    """
        The Destination class can be seen as a simple structure which holds a IP or Domain address and port.
        Address and port combinations are often delivered in as tulpe or array, but a Destination object is
        are clearer way to represent de address/port combination. The Destination class in used to communicate
        target and proxy addresses to AttackMethods and Proxy's
    """
    def __init__(self, address, port):
        """
            Creates a new Destination instance

            :param address: IP/Domain (string)
            :param port: Port (int or string)
        """
        self._address = address
        try:
            self._port = int(port)
        except ValueError:
            raise ValueError("Could not convert the port to an integer value.")

    @property
    def address(self):
        """
            Get the address

            :return: The address (string)
        """
        return self._address

    @property
    def port(self):
        """
            Get the port

            :return: The port (int)
        """
        return self._port

    def __str__(self):
        return "Destination with an address of " + self._address + " and a port of " + str(self._port)

