from Protocol import Protocol


class NoProtocol(Protocol):
    """
        The NoProtocol class has the same role as the NoProxy class. The NoProtocol class is a wrapper around a bytes
         array so classes can treat it like any other protocol. This makes working with protocol objects easier.
    """
    def __init__(self, my_bytes):
        Protocol.__init__(self)
        self._bytes = my_bytes

    def __str__(self):
        return self._bytes.decode()

    def get_bytes(self):
        return self._bytes
