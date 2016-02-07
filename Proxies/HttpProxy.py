from copy import copy
from Protocols.HttpProtocol import *
from Proxy import Proxy, ProxyError


class HttpProxy(Proxy):
    """
        The HttpProxy class can be used to route http traffic through a http proxy server.
        Examples of (http) proxy servers are:

            Burp suite - https://portswigger.net/burp/
            WebScarab - https://www.owasp.org/index.php/Category:OWASP_WebScarab_Project
            Squid proxy - http://www.squid-cache.org/

         Not all methods are documented because they are already documented in the Proxy class.

         Authentication is not supported at the moment, but will be added at a later date.
    """
    def __init__(self, proxy_address):
        """
            Constructor. Initiates a new HttpProxy class which will use the given proxy address to send requests to.
            :param proxy_address: Address of the proxy which you want to use to send you traffic through (Destination
            object)
        """
        super(HttpProxy, self).__init__(proxy_address)
        self._proxy_socket = None
        self._destination = None

    def _connect(self, destination):
        self._proxy_socket = self._init_connection(self._proxy_address.address, self._proxy_address.port)
        self._destination = destination

    def is_connected(self):
        return self._proxy_socket is not None

    def _send(self, payload):
        prepped_payload = self._prepare_payload(payload)
        self._proxy_socket.sendall(prepped_payload.get_bytes())

    def _prepare_payload(self, payload):
        if not isinstance(payload, HttpRequest):
            payload = convert_http_str_to_request_obj(payload.__str__())
        else:
            # Create a copy of the payload object because the payload will be changed by the add_host_header and
            # add_domain_to_url method. The changes will reflect back at the caller of this method if no copy is created.
            payload = copy(payload)
        self._add_host_header(payload)
        self._add_domain_to_url(payload)
        return payload

    def _add_host_header(self, request):
        """
            Add a Host entry to the http header.
            :param request: The http request to add the Host entry to
        """
        host_header = collections.OrderedDict()
        host_header['Host'] = self._destination.address
        self._add_port_if_needed(host_header['Host'])
        host_header.update(request.headers)
        request.headers = host_header

    def _add_domain_to_url(self, request):
        """
            Adds the domain (and port) of the destination to the http request. Example:

                GET /index.html HTTP/1.0

                becomes:

                GET http://example.com/index.html HTTP/1.0

            :param request: The http changed http request
        """
        absolute_url = request.url
        request.url = "http://" + self._destination.address
        self._add_port_if_needed(request.url)
        request.url += absolute_url

    def _receive(self):
        answer = self._read_until_empty(self._proxy_socket)
        answer = answer.decode()
        response = convert_http_str_to_response_obj(answer)
        has_error, msg = self._check_resp_for_errors(response)
        if has_error:
            raise ProxyError(msg)
        else:
            return response

    def _check_resp_for_errors(self, response):
        if response.status_code > 400:
            return (True, 'Received error code in the http response. Code: ' + str(response.status_code) + \
                    ' Message: ' + response.status_msg)
        else:
            return False, None

    def _add_port_if_needed(self, url_str):
        """
            Add a port to a url_string if the destination port is not 80 (default http port)
        """
        if self._destination.port is not 80:
            url_str += ":" + str(self._destination.port)

    def _close(self):
        self._proxy_socket.close()
        self._proxy_socket = None

    def copy(self):
        return HttpProxy(self._proxy_address)
