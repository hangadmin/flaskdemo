import requests.exceptions
import six

from functools import partial

DEFAULT_TIMEOUT_SECONDS = 180


class dyClient(requests.Session):
    def __init__(self, base_url=None, timeout=DEFAULT_TIMEOUT_SECONDS):
        super(dyClient, self).__init__()

        self.base_url = base_url
        self.timeout = timeout

    def myPost(self, url, **kwargs):
        return self.post(url, **self._set_request_timeout(kwargs))

    def myGet(self, url, **kwargs):
        return self.get(url, **self._set_request_timeout(kwargs))

    def myDelete(self, url, **kwargs):
        return self.delete(url, **self._set_request_timeout(kwargs))

    def _set_request_timeout(self, kwargs):
        """Prepare the kwargs for an HTTP request by inserting the timeout
        parameter, if not already present."""
        kwargs.setdefault('timeout', self.timeout)
        return kwargs

    def myUrl(self, pathfmt, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, six.string_types):
                raise ValueError(
                    'Expected a string but found {0} ({1}) '
                    'instead'.format(arg, type(arg))
                )

        quote_f = partial(six.moves.urllib.parse.quote_plus, safe="/:")
        args = map(quote_f, args)

        return '{0}{1}'.format(self.base_url, pathfmt.format(*args))

    def result(self, response, json=False, binary=False):
        assert not (json and binary)

        if json:
            return response.json()
        if binary:
            return response.content
