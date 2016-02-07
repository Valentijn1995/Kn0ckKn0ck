from Proxies.Protocols.HttpProtocol import *
from unittest import TestCase


class TestHttpProtocol(TestCase):
    def setUp(self):
        self._request_string = "GET / HTTP/1.1\r\n" \
                               "Host: google.com\r\n" \
                               "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0\r\n" \
                               "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n" \
                               "Accept-Language: nl,en-US;q=0.7,en;q=0.3\r\n" \
                               "Accept-Encoding: gzip, deflate\r\n" \
                               "DNT: 1\r\n" \
                               "Connection: close\r\n\r\n"

        self._response_string = "HTTP/1.1 302 Found\r\n" \
                                "Cache-Control: private\r\n" \
                                "Content-Type: text/html; charset=UTF-8\r\n" \
                                "Location: http://www.google.nl/?gfe_rd=cr&ei=xqGaVusehonxB635p-AL\r\n" \
                                "Content-Length: 256\r\n" \
                                "Date: Sat, 16 Jan 2016 20:02:14 GMT\r\n" \
                                "Server: GFE/2.0\r\n" \
                                "Connection: close\r\n\r\n" \
                                "<HTML><HEAD><meta http-equiv='content-type' content='text/html;charset=utf-8'>\r\n" \
                                "<TITLE>302 Moved</TITLE></HEAD><BODY>\r\n" \
                                "<H1>302 Moved</H1>\r\n" \
                                "The document has moved\r\n" \
                                "<A HREF='http://www.google.nl/?gfe_rd=cr&amp;ei=xqGaVusehonxB635p-AL'>here</A>.\r\n" \
                                "</BODY></HTML>"

    def test_http_request_error(self):
        with self.assertRaises(ValueError):
            HttpRequest(method="BLABLA")

    def test_http_response_error(self):
        with self.assertRaises(ValueError):
            HttpResponse(123456)

    def test_convert_response(self):
        convert_http_str_to_response_obj(self._response_string)

    def test_convert_request(self):
        convert_http_str_to_request_obj(self._request_string)

    def tearDown(self):
        pass
