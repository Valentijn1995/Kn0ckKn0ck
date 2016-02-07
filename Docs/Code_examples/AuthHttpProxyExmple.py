from Proxies.Destination import Destination
from Proxies.AuthHttpProxy import AuthHttpProxy
from Proxies.Protocols.HttpProtocol import *

my_proxy_address = Destination("127.0.0.1", 3128)  # port 3128 is the default port for Squid proxy
my_proxy = AuthHttpProxy(my_proxy_address, "basic", "admin", "password")

my_http_request = HttpRequest("GET", "/", ExampleHttpHeaders['default'])

my_proxy.connect(Destination("google.com", 80))
my_proxy.send(my_http_request)
response = my_proxy.receive()
print response

