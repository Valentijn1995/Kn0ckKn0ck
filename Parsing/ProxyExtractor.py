from Proxies import ProxyFactory
from random import shuffle


class ProxyExtractor:
    """
        The ProxyExtractor is responsible for converting the data (supplied by a Reader) to Proxy objects.

        The data has to contain the following properties: Address, Port, Type, Auth method, Username, Password.
    """

    def __init__(self, reader):
        """
            Initiate a new ProxyExtractor instance with the given Reader object.

            :param reader: The Reader object where the ProxyExtractor needs to read the proxy data from
        """
        self._reader = reader

    def get_proxy(self, index):
        """
            Get a proxy object at a given index in de proxy file.
            So if you want the second proxy in de proxy file, you will need to call this method like this:
            get_proxy(1). The count starts at zero (same way as lists).

            :param index: index of the wanted proxy (int value)
            :return: The Proxy object at the given index
        """
        address = self._reader.get_value('Address', index)
        port = self._reader.get_value('Port', index)
        proxy_type = self._reader.get_value('Type', index)
        # Only parse the authorization properties if Auth method is defined
        if self._reader.value_exists('Auth method'):
            auth_method = self._reader.get_value('Auth method', index)
            auth_user = self._reader.get_value('Username', index)
            auth_pass = self._reader.get_value('Password', index)
            proxy = ProxyFactory.create_proxy(address, port, proxy_type, auth_method=auth_method, username=auth_user,
                                              password=auth_pass)
        else:
            proxy = ProxyFactory.create_proxy(address, port, proxy_type)
        return proxy

    def get_all_proxies(self):
        """
            Get all the proxies from the Reader.

            :return: A list filled with all the proxy objects extracted from the Reader
        """
        proxy_list = []
        max_range = self.get_proxy_count()
        for index in range(0, max_range, 1):
            proxy = self.get_proxy(index)
            proxy_list.append(proxy)
        return proxy_list

    def get_all_proxies_randomised(self):
        """
            Almost the same as the get_all_proxies method but this method randomises the proxies in the list before
            returning them. This method uses the shuffle method in the Python random module.

            :return: A randomised list of all the proxies
        """
        proxy_list = self.get_all_proxies()
        shuffle(proxy_list)
        return proxy_list

    def get_proxy_count(self):
        """
            Get the amount of proxies.

            :return: The amount of proxies (as int)
        """
        return self._reader.get_count()
