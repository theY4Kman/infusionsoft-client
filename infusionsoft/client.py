import logging
import socket

from xmlrpc.client import ServerProxy, ProtocolError, Fault

logger = logging.getLogger(__name__)


class DefaultArgServerProxy(ServerProxy, object):
    """Pass positional args to all method calls"""

    def __init__(self, *args, **kwargs):
        self.__default_args = tuple(kwargs.pop('default_args', ()))
        super(DefaultArgServerProxy, self).__init__(*args, **kwargs)
        self.__real_request = self._ServerProxy__request
        self._ServerProxy__request = self.__request

    def __request(self, methodname, args):
        args = self.__default_args + tuple(args)
        return self.__real_request(methodname, args)


class RetryServerProxy(ServerProxy, object):
    """Retry failed method calls a number of times"""

    def __init__(self, *args, **kwargs):
        """
        :param retries: number of times to *retry* a request (i.e. a value of 2
            means there will be 3 total attempts before failing)
        """
        self.__retries = kwargs.pop('retries', 2)
        super(RetryServerProxy, self).__init__(*args, **kwargs)
        self.__real_request = self._ServerProxy__request
        self._ServerProxy__request = self.__request

    def __request(self, methodname, args):
        retries_left = self.__retries
        while True:
            try:
                return self.__real_request(methodname, args)
            except (ProtocolError, Fault, socket.error) as exc:
                if isinstance(exc, Fault):
                    # Retry request on InvalidConfig (a false, infrequent fault)
                    if '[InvalidConfig]' not in exc.faultString:
                        raise

                if retries_left == 0:
                    raise
                else:
                    retries_left -= 1
                    continue


class InfusionsoftServerProxy(RetryServerProxy, DefaultArgServerProxy):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('encoding', 'utf-8')
        kwargs.setdefault('allow_none', False)
        kwargs.setdefault('use_datetime', True)
        super().__init__(*args, **kwargs)


def get_client(api_url: str, api_key: str, client_cls=InfusionsoftServerProxy):
    return client_cls(api_url, default_args=[api_key])
