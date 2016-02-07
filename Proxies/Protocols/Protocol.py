import abc


class Protocol:
    """
        The Protocol class is an abstract class which represents a protocol. A protocol can by anything. Examples
         of protocols are: http, socks, ftp, dns and ntp. Protocol objects are often send through proxy classes.
         Proxy classes can try to convert the protocol or add information to it. Take te HttpProxy class for example.
         The HttpProxy class makes use of the Http protocol. It adds proxy information to a given http request and
         sends it of. Different protocol objects can be nested inside each other.
    """
    def __init__(self):
        """
            Creates a new Protocol object.
        """
        pass

    @abc.abstractmethod
    def get_bytes(self):
        """
            Get a byte representation of the protocol.
        """
        return
