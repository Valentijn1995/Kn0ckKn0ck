from HttpProxy import HttpProxy
from AuthHttpProxy import AuthHttpProxy
from NoProxy import NoProxy
from DebugProxy import DebugProxy
from Proxies.Destination import Destination


def create_proxy(proxy_address="127.0.0.1", proxy_port=8080, proxy_name="no-proxy", **kargs):
    """
        The ProxyFactory can be used to create ProxyObjects.

        :param proxy_address: The address of the proxy-server (default= "127.0.0.1")
        :param proxy_port: The port of the proxy-server (default= 8080)
        :param proxy_name: The proxy name (default= no-proxy)
        :param kargs: extra arguments for the proxy factory. The arguments depend on the type of proxy that you want
                        to use
        :return: A newly created Proxy object
    """
    # Create destination object with the address and port
    proxy_dest = Destination(proxy_address, proxy_port)

    if proxy_name == "no-proxy":
        return NoProxy()
    elif proxy_name == "http-proxy":
        if "auth_method" in kargs and kargs["auth_method"] != "none":
            return AuthHttpProxy(proxy_dest, kargs["auth_method"], kargs["username"], kargs["password"])
        else:
            return HttpProxy(proxy_dest)
    elif proxy_name == "socks-proxy":
        raise NotImplementedError("Socks proxies are not supported yet")
    elif proxy_name == "debug-proxy":
        return DebugProxy()
    else:
        raise ValueError(proxy_name + " was not recognised as a valid proxy name")
