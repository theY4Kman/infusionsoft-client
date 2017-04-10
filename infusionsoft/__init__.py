import sys
from xmlrpc.client import ServerProxy

from lazy_object_proxy import Proxy

from infusionsoft.client import get_client, InfusionsoftServerProxy


# Expose stubs
from infusionsoft.stubs import *


class InitializeMixin:
    def initialize(self, api_url: str, api_key: str):
        global _client
        _client = get_client(api_url, api_key, client_cls=InitializedServerProxy)
        client.__wrapped__ = _client


class InitializedServerProxy(InitializeMixin, InfusionsoftServerProxy):
    pass


class UninitializedServerProxy(InitializeMixin, ServerProxy, object):
    def __init__(self, *args, **kwargs):
        super().__init__('http://uninitialized', *args, **kwargs)
        self.__real_request = self._ServerProxy__request
        self._ServerProxy__request = self.__request

    def __request(self, methodname, args):
        raise ValueError('Please call infusionsoft.initialize first.')


_client = UninitializedServerProxy()
client = Proxy(lambda: _client)

# Django's runserver reloader requires this property
client.__file__ = __file__


# Expose XML-RPC client as `infusionsoft` module
sys.modules[__name__] = client
