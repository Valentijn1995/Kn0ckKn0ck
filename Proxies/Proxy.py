import abc
import socket


class ProxyError(Exception):
    pass


class Proxy(object):
    """
        The Proxy class serves as a template for the implementation of specific proxy's. The Proxy class is an abstract
        class, so it can not function on its own. The HttpProxy class is an example which is based on this class.
    """

    def __init__(self, proxy_address):
        """
            Constructor. Normally called from the child.

            :param proxy_address: The address of the proxy in the form of a Destination object.
        """
        self._proxy_address = proxy_address

    # Begin helper methods. These methods automate repeating tasks. The methods are shared with all classes that
    # extend from this class. Helper methods are usually static.

    @staticmethod
    def _init_connection(ip, port):
        """
            Method for initiating a standard ipv4 streaming socket.

            :param ip: The ip of the target
            :param port: The port of the target
            :return: A new socket object
        """
        try:
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            my_socket.connect((ip, port))
        except socket.error as error:
            raise ProxyError("Failed to connect to " + ip + ":" + str(port) + ". " + str(error))
        return my_socket

    @staticmethod
    def _read_until_empty(socket_obj, buffer_size=1024):
        """
            Method for reading from a socket until the buffer is empty.

            :param socket_obj: The socket object to read from
            :param buffer_size: The size of the buffer which is used to read from the socket (default= 1024)
            :return: The received bytes
        """
        if socket_obj:
            response = b""
            while True:
                data = socket_obj.recv(buffer_size)
                if not data:
                    break
                response += data
            return response
        else:
            raise ValueError("socket_obj can not be empty")

    # End helper methods.

    # Begin abstract methods. These methods have to be implemented by the class which extends from the Proxy class.
    # The children of from this class can make used of the helper methods to make the implementation easier.

    def connect(self, destination):
        """
            Connect to the given destination.

            :param destination: The target destination (Destination object)
        """
        self.close()
        self._connect(destination)

    @abc.abstractmethod
    def _connect(self, destination):
        return

    @abc.abstractmethod
    def is_connected(self):
        """
            Checks if the proxy is connected to a destination.

            :return: True if the proxy is connected to a destination or False if the proxy is not connected.
        """
        return

    def send(self, payload):
        """
            Send the given payload to the destination (use after the connect method).

            :param payload: The payload to send to the target destination
        """
        if self.is_connected():
            self._send(payload)
        else:
            raise ProxyError("First call the connect method before sending anything")

    @abc.abstractmethod
    def _send(self, payload):
        return

    def receive(self):
        """
            Receive the answer from the other side of the connection.
        """
        if self.is_connected():
            return self._receive()
        else:
            raise ProxyError("First call the connect method before receiving anything")

    @abc.abstractmethod
    def _receive(self):
        return

    def close(self):
        """
            Close the connection. You can connect to another destination by using the connect method.
        """
        if self.is_connected():
            self._close()

    @abc.abstractmethod
    def _close(self):
        return

    @abc.abstractmethod
    def copy(self):
        """
            Creates a new proxy object with the same configuration and returns it.

            :return: A copy of the proxy object
        """
        return

        # End abstract methods.
