import Proxies.Destination
import Proxies.HttpProxy
from Proxies.Protocols.HttpProtocol import ExampleHttpHeaders

my_proxy_address = Proxies.Destination.Destination("127.0.0.1", 8080)
my_proxy = Proxies.HttpProxy.HttpProxy(my_proxy_address)

my_http_request = Proxies.HttpProxy.HttpRequest("GET", "/", ExampleHttpHeaders['default'])

my_proxy.connect(Proxies.Destination.Destination("google.com", 80))
my_proxy.send(my_http_request)
response = my_proxy.receive()
print response

