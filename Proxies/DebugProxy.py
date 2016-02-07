from Proxy import Proxy


class DebugProxy(Proxy):
    """
        Proxy used for Debugging and Testing purposes. This proxy is normally not used in a production environment.
    """

    def __init__(self, print_to_console=True):
        """
            Constructor.

            :param print_to_console: Indicates if the debug proxy has to print feedback to the console. Set it to True
            if you want the DebugProxy to print feedback to the console when you call a method. Set it to False if you
            don't want the DebugProxy to print to the console.
        """
        super(DebugProxy, self).__init__(None)
        self._payload = None
        self._connected = False
        self._print_to_console = print_to_console

    def is_connected(self):
        return self._connected

    def _send(self, payload):
        self._payload = payload
        self._pr_if_needed("Sent called. Payload: " + payload.__str__())

    def _connect(self, destination):
        self._connected = True
        self._pr_if_needed("Connect called")

    def copy(self):
        self._pr_if_needed("Copy method called")
        return DebugProxy(self._proxy_address)

    def _close(self):
        self._connected = False
        self._pr_if_needed("Close called")

    def _receive(self):
        if self._payload is not None:
            self._pr_if_needed("Receive called. Returning the following payload: " + self._payload.__str__())
            return self._payload

    def _pr_if_needed(self, pr_str):
        """
            pr_if_needed stands for print_if_needed. This method prints the given string parameter to the console if
            the self._print_to_console value is set to True. The method does nothing if self._print_to_console value
            is False.

            :param pr_str: the string to be printed (if needed).
        """
        if self._print_to_console is True:
            print "DebugProxy: " + pr_str

