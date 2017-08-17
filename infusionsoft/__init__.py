import functools
import sys
from xmlrpc.client import ServerProxy, _Method

from infusionsoft.vendor.werkzeug.local import LocalProxy
from infusionsoft.client import get_client, InfusionsoftServerProxy


# Import submodules before overriding "infusionsoft" in sys.modules
import infusionsoft.query
import infusionsoft.client
import infusionsoft.stubs

query = infusionsoft.query
client = infusionsoft.client
stubs = infusionsoft.stubs

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
def initialize(api_url: str, api_key: str, **options): pass


__all__ += ['query', 'gen_stubs', 'client', 'contrib', 'is_initialized']


class _Service(_Method):
    def __init__(self, send, name):
        super(_Service, self).__init__(send, name)
        self._wrapped = getattr(stubs, name, None)
        self._methods = {}

    def __dir__(self):
        return dir(self._wrapped)

    def __getattr__(self, name):
        if name not in self._methods:
            wrapped = getattr(self._wrapped, name, None)
            if wrapped:
                class _WrappedMethod(_Method):
                    @functools.wraps(wrapped)
                    def __call__(self, *args):
                        return super(_WrappedMethod, self).__call__(*args)

                rpc_name = '{}.{}'.format(self._Method__name, name)
                method =_WrappedMethod(self._Method__send, rpc_name)
            else:
                method = super(_Service, self).__getattr__(name)
            self._methods[name] = method

        return self._methods[name]


class StubMixin:
    def __dir__(self):
        return stubs.__all__

    def __getattr__(self, service):
        return _Service(self._ServerProxy__request, service)


class InitializeMixin:
    _real_module = sys.modules[__name__]

    # Play nicely with conventions
    __version__ = __version__
    __name__ = __name__
    __path__ = __path__
    __file__ = __file__

    # Django checks for a "models" submodule in the root package, cuz why not
    models = None

    # Expose submodules
    query = query
    client = client
    contrib = contrib

    def initialize(self, api_url_or_app_name: str, api_key: str, **options):
        global _api_client
        _api_client = get_client(api_url_or_app_name, api_key,
                                 client_cls=InitializedServerProxy, **options)


class InitializedServerProxy(StubMixin, InitializeMixin,
                             InfusionsoftServerProxy):
    is_initialized = True


class UninitializedServerProxy(StubMixin, InitializeMixin, ServerProxy):
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
