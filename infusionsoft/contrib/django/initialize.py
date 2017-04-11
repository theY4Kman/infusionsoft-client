from django.conf import settings


def initialize():
    """Initialize the client from Django settings once"""
    import infusionsoft

    if not infusionsoft.is_initialized:
        try:
            api_url = settings.INFUSIONSOFT_API_URL
            api_key = settings.INFUSIONSOFT_API_KEY
        except AttributeError:
            raise ValueError('Please set INFUSIONSOFT_API_URL and '
                             'INFUSIONSOFT_API_KEY in your settings')
        else:
            infusionsoft.initialize(api_url, api_key)
