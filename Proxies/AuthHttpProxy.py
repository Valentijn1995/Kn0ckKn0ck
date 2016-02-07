from HttpProxy import HttpProxy
import base64

PossibleAuthMethods = ('basic', 'digest')


class AuthHttpProxy(HttpProxy):
    def __init__(self, proxy_address, auth_method, auth_username, auth_password):
        super(AuthHttpProxy, self).__init__(proxy_address)
        if auth_method == 'digest':
            raise NotImplementedError("Digest authorization has not been implemented yet")
        elif auth_method not in PossibleAuthMethods:
            raise ValueError("The given auth_method is not supported by this proxy")
        self._method = auth_method
        self._username = auth_username
        self._password = auth_password
        self._token = None

    def _prepare_payload(self, payload):
        prepped_payload = super(AuthHttpProxy, self)._prepare_payload(payload)
        if self._method == "basic":
            prepped_payload.headers['Proxy-Authorization'] = "Basic " + self.generate_auth_token()
        elif self._method == "digest":
            pass  # TODO implement digest
        return prepped_payload

    def generate_auth_token(self):
        if self._token is None:
            user_pass_str = self._username + ":" + self._password
            self._token = base64.standard_b64encode(user_pass_str)  # save token for performance reasons
        return self._token

    def copy(self):
        return AuthHttpProxy(self._proxy_address, self._method, self._username, self._password)
