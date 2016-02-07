import re
import collections
from Protocol import Protocol
from NoProtocol import NoProtocol

"""
    This python file contains components for working with the http protocol. This file contains the following:

    - The HttpRequest and HttpResponse classes for manipulating, reading and creating http requests and responses.
    - Methods for converting raw http data to HttpRequest and HttpResponse objects.
    - Sample http request headers.
"""

# Example http headers which can be used for creating http requests.
ExampleHttpHeaders = {
    'default': collections.OrderedDict([
        ('User-Agent', 'kn0ckkn0ck'),
        ('Accept', 'text/html'),
        ('Accept-Language', 'en-US'),
        ('Accept-Encoding', 'gzip, deflate'),
        ('Cache-Control', 'max-age=0, no-cache, must-revalidate, proxy-revalidate'),  # Prevents (proxy) caching
        ('Connection', 'close')
    ])
}

# source link: https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html
HttpRequestMethods = ('OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT')


class HttpRequest(Protocol):
    """
        This class represents a http request. The class contains a method, url, headers and payload.
    """

    def __init__(self, method="GET", url="/", headers=ExampleHttpHeaders['default'], payload=None):
        """
            Initiates a new http request object.

            :param method: HTTP method: GET, POST, PUT, ...
            :param url: The request url
            :param headers: a dictionary with header values. See the SampleHttpHeaders variable for an example
            :param payload: The http payload as a Protocol object
        """
        Protocol.__init__(self)
        if method not in HttpRequestMethods:
            raise ValueError('The method ' + method + ' is not recognised as a valid http method')
        self.method = method
        self.url = url
        self.headers = headers
        self.payload = payload

    def __str__(self):
        """
            Returns the http request as a string. The string contains normal line endings ("\n").

            :return: http request in string form
        """
        method_header = self.method + " " + self.url + " HTTP/1.0\n"
        custom_headers = ""
        if len(self.headers) > 0:
            for header_name, header_value in self.headers.iteritems():
                custom_headers += (header_name + ": " + header_value + "\n")
        request_str = method_header + custom_headers + "\n"
        if self.payload:
            request_str += self.payload.__str__()
        return request_str

    def get_bytes(self):
        """
            Returns a byte representation of the http request. Used for sending the request to a socket.
             Note: this function uses "\r\n" line endings and not "\n" line endings because the "/r/n" line endings
             have to be used acording to the http protocol guidelines. Proxies will not understand the http request if
             you use "\n" line endings.

            :return:
        """
        method_header = self.method.encode() + b" " + self.url.encode() + b" HTTP/1.0\r\n"
        custom_headers = b""
        if len(self.headers) > 0:
            for header_name, header_value in self.headers.iteritems():
                custom_headers += (header_name.encode() + b": " + header_value.encode() + b"\r\n")
        request_bytes = method_header + custom_headers + b"\r\n"
        if self.payload:
            request_bytes += self.payload.get_bytes()
        return request_bytes

HttpStatusCodes = {100: 'Continue', 101: 'Switching Protocols', 200: 'OK', 201: 'Created', 202: 'Accepted',
                   203: 'Non-Authoritative Information', 204: 'No Content', 205: 'Reset Content',
                   206: 'Partial Content', 300: 'Multiple Choices', 301: 'Moved Permanently', 302: 'Found',
                   303: 'See Other', 304: 'Not Modified', 305: 'Use Proxy', 307: 'Temporary Redirect',
                   400: 'Bad Request', 401: 'Unauthorized', 402: 'Payment Required', 403: 'Forbidden', 404: 'Not Found',
                   405: 'Method Not Allowed', 406: 'Not Acceptable', 407: 'Proxy Authentication Required',
                   408: 'Request Timeout', 409: 'Conflict', 410: 'Gone', 411: 'Length Required'}


class HttpResponse(Protocol):
    """
        This class represents a http response and works the same as the HttpRequest class but has other properties.
    """

    def __init__(self, status_code, headers=None, payload=None):
        """
            Creates as new http response.

            :param status_code: Status code: 200, 404, 302, 400, ...
            :param headers: Headers of the response as a dictionary object
            :param payload: Payload as Protocol object
        """
        Protocol.__init__(self)
        self.status_code = int(status_code)
        if HttpStatusCodes.has_key(self.status_code):
            self.status_msg = HttpStatusCodes[self.status_code]
        else:
            raise ValueError('Status code ' + str(self.status_code) + ' is not recognised as a valid http status code')
        self.headers = headers
        self.payload = payload

    def __str__(self):
        """
            Returns the http response as a string. Uses the "\n" line ending.
        """
        method_header = "HTTP/1.0 " + str(self.status_code) + " " + self.status_msg + "\n"
        custom_headers = ""
        if self.headers is not None:
            for header_name, header_value in self.headers.iteritems():
                custom_headers += (header_name + ": " + header_value + "\n")
        return method_header + custom_headers + "\n" + self.payload.__str__()

    def get_bytes(self):
        """
            Returns the http response as bytes. Uses the "\r\n" line ending.
        """
        method_header = b"HTTP/1.0 " + str(self.status_code).encode() + b" " + self.status_msg.encode() + b"\r\n"
        custom_headers = b""
        if self.headers is not None:
            for header_name, header_value in self.headers.iteritems():
                custom_headers += (header_name.encode() + b": " + header_value.encode() + b"\r\n")
        response_bytes = method_header + custom_headers + b"\r\n"
        if self.payload:
            response_bytes += self.payload.get_bytes()


# The HttpRequestRegex is used for parsing a http request.
HttpRequestRegex = re.compile(
    '(?P<method>.*) (?P<url>.*) HTTP/1\..\r\n(?P<headers>(.*:.*\r\n)*)\r\n(?P<payload>.*)')
# Regular expression for parsing http responses.
HttpResponseRegex = re.compile(
    'HTTP/1\.. (?P<response_code>...) (?P<response_name>.*)\r\n(?P<headers>(.*: .*\r\n)*)\r\n(?P<payload>.*)')


def convert_http_str_to_request_obj(http_str):
    """
        Converts a http request string to a HttpRequest object.
        This method uses the HttpRequestRegex to parse the http string.

        :param http_str: The http request in the form of a string
        :return: The converted http request as a HttpRequest object
    """
    result = HttpRequestRegex.match(http_str)
    if result:
        method = result.group('method')
        url = result.group('url')
        raw_headers = result.group('headers')
        payload = result.group('payload')

        headers = _parse_http_header(raw_headers)
        request = HttpRequest(method, url, headers, NoProtocol(payload))
        return request
    else:
        raise ValueError("Could not parse the http request with the HttpRequestRegex regular expression. Please"
                         "check the correctness of the http request. The received request: " + http_str)


def convert_http_str_to_response_obj(http_str):
    """
        Converts a http response string to a HttpResponse object.

        :param http_str: The http response string
        :return: The converted http response in the form of a HttpResponse object
    """
    result = HttpResponseRegex.match(http_str)
    if result:
        response_code = result.group('response_code')
        raw_headers = result.group('headers')
        payload = result.group('payload')

        headers = _parse_http_header(raw_headers)
        response = HttpResponse(response_code, headers, NoProtocol(payload))
        return response
    else:
        raise ValueError("Could not parse the http response with the HttpResponseRegex regular expression. Please"
                         "check the correctness of the http response. The received response: " + http_str)


def _parse_http_header(header_str):
    """
        Converts the http response and request headers to a dictionary form.
        The convert_http_str_ti_response_obj and convert_http_str_to_request_obj methods use this method for parsing
        the header part of a request or response.

        :param header_str: The header as a string
        :return: The header as a dictionary
    """
    return_headers = collections.OrderedDict()
    headers = header_str.split('\n')
    for header in headers:
        key_value_pair = header.split(': ', 1)
        if len(key_value_pair) is 2:
            return_headers[key_value_pair[0]] = key_value_pair[1]
    return return_headers

