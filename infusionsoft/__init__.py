import sys
from xmlrpc.client import ServerProxy

from infusionsoft.vendor.werkzeug.local import LocalProxy
from infusionsoft.client import get_client, InfusionsoftServerProxy


# Import submodules before overriding "infusionsoft" in sys.modules
import infusionsoft.query
import infusionsoft.gen_stubs
import infusionsoft.client

query = infusionsoft.query
gen_stubs = infusionsoft.gen_stubs
client = infusionsoft.client

try:
    import infusionsoft.contrib
except ImportError:
    contrib = None
else:
    contrib = infusionsoft.contrib

# Expose stubs
from infusionsoft.stubs import *
from infusionsoft.stubs import __all__

from infusionsoft.version import __version__


# Stub. The actual values are exposed by Initialized/UninitializedServerProxy.
is_initialized = False
def initialize(api_url: str, api_key: str): pass


__all__ += ['query', 'gen_stubs', 'client', 'contrib', 'is_initialized']


class InitializeMixin:
    # Play nicely with conventions
    __version__ = __version__
    __name__ = __name__
    __path__ = __path__
    __file__ = __file__

    # Django checks for a "models" submodule in the root package, cuz why not
    models = None

    # Expose submodules
    query = query
    gen_stubs = gen_stubs
    client = client
    contrib = contrib

    def initialize(self, api_url: str, api_key: str):
        global _api_client
        _api_client = get_client(api_url, api_key, client_cls=InitializedServerProxy)


class InitializedServerProxy(InitializeMixin, InfusionsoftServerProxy):
    is_initialized = True


class UninitializedServerProxy(InitializeMixin, ServerProxy, object):
    is_initialized = False

    def __init__(self, *args, **kwargs):
        super().__init__('http://uninitialized', *args, **kwargs)
        self.__real_request = self._ServerProxy__request
        self._ServerProxy__request = self.__request

    def __request(self, methodname, args):
        raise ValueError('Please call infusionsoft.initialize first.')


_api_client = UninitializedServerProxy()
api_client = LocalProxy(lambda: _api_client, 'infusionsoft')


# Expose XML-RPC client as `infusionsoft` module
del sys.modules[__name__]
sys.modules[__name__] = api_client
